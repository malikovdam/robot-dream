{-# LANGUAGE UnicodeSyntax #-}
{-# LANGUAGE ExistentialQuantification #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE MultiParamTypeClasses #-}
module Engine where

import Control.Monad (forever, guard)
import Data.Functor ((<$>))
import Data.List (find, delete)
import Data.Maybe (fromMaybe)

import Commands
import Rules


instance CanMatch (IfDo (Reading -> Bool) a) Reading where
  matches (IfDo f _) = f

instance CanMatch (IfDoThen (Reading -> Bool) a) Reading where
  matches (IfDoThen (IfDo f _) _) = f


-- THE ENGINE --
-- | An existential data type that unifies IfDo and IfDoThen rules.
-- It's useful for instinctive and learned layers as they can ignore then-part of a rule.
data Rule = ∀ a . (CanMatch a Reading, Actionable a Command) => Rule a

instance CanMatch Rule Reading where
  matches (Rule a) = matches a

instance Actionable Rule Command where
  getAction (Rule a) = getAction a


-- | Instinctive behaviour: just perform the first rule that matches current situation.
instinctiveAction :: [Rule] -> Reading -> Command
instinctiveAction db r = fromMaybe (Forward 0.5) $ getAction <$> find (`matches` r) db

-- | Searches for a sequence of actions that leads to desired situation.
-- Useful for deliberative thinking.
chainForward :: (Eq c, Eq a) => [IfDoThen c a] -> c -> c -> [a]
chainForward []    _     _    = []
chainForward rules start goal = do
  r <- rules              -- try all available rules
  guard $ matches r start -- reject `r` and backtrack unless it matches current condition
  let res = outcome r
  let a   = action $ rule r
  if res == goal
    then return a
    else a : chainForward (delete r rules) (condition $ rule r) goal


initialDB :: [Rule]
initialDB = [Rule $ IfDo (Barrier True) (CClockwise (pi/6))]

engine :: Script ()
engine = forever $ do
  r <- readInput "One" -- FIXME: there should be no parameter here. I suggest polling all the ports.
  let c = instinctiveAction initialDB r
  executeCommand c

module Driver.Console where

import Commands

instance Driver IO where
  initialize = return ()

  output chrs = print

  input val = do
--    l <- getLine
    let (s1 : s2 : rest) = words val
    case s1 of
        "Barrier" -> return $ Barrier (read s2)
        "Light"   -> return $ Light (read s2)
        _         -> return $ Custom s1 (unwords $ s2:rest)

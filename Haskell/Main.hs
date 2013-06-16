-- So much effort has been put into this program, it's unbelievable

import System.Exit

main = do
    putStrLn "Planetary: Some sort of game"
    putStrLn "Pick something from this menu:"
    putStrLn "(1) Start Game\n(2) Continue Game\n(3) Exit"
    choice <- getLine
    case choice of  "1" -> putStrLn "There is no game"
                    "2" -> putStrLn "You haven't played the game yet"
                    "3" -> exitSuccess
                    otherwise -> putStrLn "That's not an option, try again"
    main


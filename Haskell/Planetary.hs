-- Copyright (c) 2013, Spacecow Gaming

import System.Exit
import qualified Data.Map as M
import qualified Data.List as L

-- Self explanatory main menu
main :: IO ()
main = do
    putStrLn "Planetary: Some sort of game"
    putStrLn "Pick something from this menu:"
    putStrLn "(1) Start Game\n(2) Continue Game\n(3) Exit"
    choice <- getLine
    case choice of  "1" -> start initialState
                    "2" -> putStrLn "You haven't played the game yet"
                    "3" -> exitSuccess
                    otherwise -> putStrLn "That's not an option, try again"

type Sector = (Int, Int)

-- A list comprehension generating an 11x11 grid of tuples
sectors :: [Sector] 
sectors = [ (x, y) | x <- [0..10], y <- [0..10] ]

-- All sector descriptions will be this until I can be bothered to do 
-- something else with them
descriptions :: [String]
descriptions = replicate (length sectors) "Nothing here."

-- Board is a map of the two things previous
initialBoard :: M.Map Sector String
initialBoard = M.fromList $ zip sectors descriptions

-- The only "mutable" data type. Of course, it isn't actually mutable, 
-- but new instances are generated every turn.
data GameState = GameState { playerPosition :: Sector
                           , turn :: Int 
                           , board :: M.Map Sector String
                           , output :: String
                           } deriving (Show)
initialState :: GameState
initialState = GameState { playerPosition = (0, 0)
                         , turn = 0 
                         , board = initialBoard
                         , output = ""}

-- Stringifies (?) the state into something more player readable
getState :: GameState -> String
getState GameState {playerPosition = p, turn = t, board = b, output = o} =
    generateMap b
    ++ o
    ++ replicate 50 '='
    ++ "\nYou are now in sector " ++ show p
    ++ "\nSector description: " ++ drop 5 (show (M.lookup p b))
    ++ "\nIt is turn " ++ show t 
    ++ "\nEnter an action: "

clear :: String
clear = replicate 100 '\n'

handleAction :: String -> String
handleAction a 
    | a == "help" = "HELP: Type help for help.\nHELP: Type move to move.\n"
    | a == "move" = "ERROR: You can't do that yet."
    | otherwise = "ERROR: That is not a valid action"

generateMap :: M.Map Sector String -> String
generateMap b = unwords $ L.intersperse "\n" $ replicate 11 $ replicate 11 '*'

start :: GameState -> IO a
start game = do
    putStrLn clear
    putStrLn $ getState game
    action <- getLine
    let newOutput = handleAction action
    let newGame = GameState { playerPosition = (0, 0)
                            , turn = turn game + 1
                            , board = board game 
                            , output = newOutput}
    start newGame
    

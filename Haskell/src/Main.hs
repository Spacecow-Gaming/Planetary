-- Copyright (c) 2013, Spacecow Gaming

import System.Exit
import qualified Data.Map as M

-- Self explanatory main menu
main :: IO ()
main = do
    putStrLn "Planetary: Some sort of game"
    putStrLn "Pick something from this menu:"
    putStrLn "(1) Start Game\n(2) Continue Game\n(3) Exit"
    choice <- getLine
    case choice of  "1" -> start
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
board :: M.Map Sector String
board = M.fromList $ zip sectors descriptions

-- The only "mutable" data type. Of course, it isn't actually mutable, 
-- but new instances are generated every turn.
data GameState = GameState { playerPosition :: Sector
                           , turn :: Int 
                           } deriving (Show)
initialState :: GameState
initialState = GameState { playerPosition = (0, 0), turn = 0 }

-- Stringifies (?) the state into something more player readable
getState :: GameState -> String
getState GameState {playerPosition = p, turn = t} =
    "You are now in sector " ++ show p ++ "\nSector description: " 
    ++ drop 5 (show (M.lookup p board)) ++ "\nIt is turn " 
    ++ show t ++ "\nEnter an action: "

start :: IO a
start = do
    putStrLn $ getState initialState
    action <- getLine
    start
    

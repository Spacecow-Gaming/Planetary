-- So much effort has been put into this program, it's unbelievable
-- Fuck you, I'm not documenting this, work it out yourself

import System.Exit
import qualified Data.Map as M

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

type Sector = (Int,Int)

sectors :: [Sector] 
sectors = [ (x,y) | x <- [0..10], y <- [0..10] ]

descriptions :: [String]
descriptions = replicate (length sectors) "Nothing here."

board :: M.Map Sector String
board = M.fromList $ zip sectors descriptions

data GameState = GameState { playerPosition :: Sector, turn :: Int } deriving (Show)

initialState :: GameState
initialState = GameState {playerPosition=(0,0), turn=0}

getState :: GameState -> String
getState GameState {playerPosition = p, turn = t} =
    "You are now in sector " ++ show p ++ "\nSector description: " ++ drop 5 (show (M.lookup p board)) ++ "\nIt is turn " ++ show t ++ "\nEnter an action: "

start :: IO a
start = do
    putStrLn $ getState initialState
    action <- getLine
    start
    

import System.Environment

-- helpter function that subtracts each element in a list from 255
subtractFrom255 :: [Int] -> [Int]
subtractFrom255 [] = []
subtractFrom255 (x:xs) =  (255-x):subtractFrom255 xs

-- main function that inverts all of the integers in the given array, this will invert the colors of the image
main :: IO ()
main = do args <- getArgs
          let numbers = map read args :: [Int]
          let result = subtractFrom255 numbers
          let resultStrings = map show result
          let outputString = unwords resultStrings
          putStrLn outputString

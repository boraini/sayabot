from dotenv import dotenv_values
import sys
from src import main

if __name__=="__main__":
    main(dotenv_values(".env"), len(sys.argv) >= 2 and sys.argv[1] == "nodiscord")

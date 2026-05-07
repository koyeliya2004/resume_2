"""Run this once to create and seed your database."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.seed_data import run_seed

if __name__ == "__main__":
    print("Setting up database...")
    run_seed()
    print("Done! Database is ready.")

import os
import sys
import subprocess
from utils import get_mileage

def load_thetas():
	path = "docs/results.txt"
	if not os.path.exists(path) or os.path.getsize(path) == 0:
		print("Thetas not found for prediction.")
		return 0,0
	try:
		with open(path) as f:
			line = f.readline().strip().split(',')
		t0 = float(line[0])
		t1 = float(line[1])
		return t0, t1
	except (IndexError, ValueError, FileNotFoundError) as e:
		print(f"Error loading thetas: {e}")
	return 0, 0

# prediction is y = t0 + t1 * x
def make_prediction(mileage, t0, t1):
	return t0 + mileage * t1


def guess(show_bonus=False):
	if show_bonus:
		print("Running training with visualization!")
		train_path = os.path.join(os.path.dirname(__file__), "train.py")
		subprocess.run(["python3", train_path, "--bonus"], check=True)

	miles = get_mileage()
	t0 = 0
	t1 = 0
	t0, t1 = load_thetas()
	prediction = make_prediction(miles, t0, t1)
	print(f"t0: {t0}, t1: {t1}")
	print(f"Mileage: {miles}\t| Price: {prediction}")

if __name__ == "__main__":
    show_bonus = len(sys.argv) > 1 and sys.argv[1] == "--bonus"
    guess(show_bonus)

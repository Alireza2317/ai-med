import pandas as pd

def get_class_distribution_info(df: pd.DataFrame, target_class) -> None:
	class_counts = df[target_class].value_counts()
	class_percentages = df[target_class].value_counts(normalize=True) * 100

	print("Class Distribution:")
	for cls, count, pct in zip(class_counts.index, class_counts.values, class_percentages.values):
		print(f"Class {int(cls)}: {count} samples ({pct:.2f}%)")
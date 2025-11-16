import seaborn as sns, matplotlib.pyplot as plt, os

NUMERIC_COLS = ["age","bmi","HbA1c_level","blood_glucose_level"]

def make_plots(df, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for c in NUMERIC_COLS:
        plt.figure(); plt.hist(df[c].dropna(), bins=30)
        plt.title(f"Histogram of {c}"); plt.savefig(os.path.join(out_dir,f"hist_{c}.png")); plt.close()
        plt.figure(); sns.boxplot(x="diabetes", y=c, data=df)
        plt.title(f"{c} by Diabetes"); plt.savefig(os.path.join(out_dir,f"box_{c}.png")); plt.close()
    prev = df.groupby("smoking_history")["diabetes"].mean()*100
    plt.figure(); prev.plot(kind="bar")
    plt.title("Diabetes % by Smoking History")
    plt.savefig(os.path.join(out_dir,"bar_smoking_diabetes.png")); plt.close()
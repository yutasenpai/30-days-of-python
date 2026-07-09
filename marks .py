print("="*70)
print("🎯--BEST OF FIVE MARKS--🎯")
print("="*70)

def best_of_five():
    subjects = ['Maths', 'Science', 'SST', 'Hindi', 'English', 'AI']
    marks = {}

    for subject in subjects:
        print("-"*70)
        print(f"\nEnter marks scored in {subject}.")

        # Validate theory marks
        while True:
            try:
                theory = float(input(f"Enter {subject} theory marks (out of 80): "))
                if 0 <= theory <= 80:
                    break
                else:
                    print(f"\nYou entered {theory}. Enter a valid number between 0 and 80.")
            except ValueError:
                print("\nEnter a valid number.")

        # Validate internal marks
        while True:
            try:
                internal = float(input(f"Enter {subject} internal marks (out of 20): "))
                if 0 <= internal <= 20:
                    break
                else:
                    print(f"\nYou entered {internal}. Enter a valid number between 0 and 20.")
            except ValueError:
                print("\nEnter a valid number.")

        print("-"*70)
        marks[subject] = theory + internal

    # Sort subjects by total marks and pick best 5
    best_five = sorted(marks.items(), key=lambda x: x[1], reverse=True)[:5]
    total = sum(score for _, score in best_five)
    percentage = (total / 500) * 100

    print("="*70)
    print("\n🎯 Best 5 subjects:")
    for subject, score in best_five:
        print(f"{subject}: {score}")
    print("="*70)
    print(f"\nTotal percentage: {percentage:.2f}%")
    print("="*70)

best_of_five()

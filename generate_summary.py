import summarizer

SUMMARY_LENGTH = 4

input_file = "input_file.txt"
# "reason_deep_learning_csv.txt" 
s = summarizer.Summarizer()
s.set_factors(10, 10, 10)
summary = s.generate_summary(input_file, SUMMARY_LENGTH)
print summary

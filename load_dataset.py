from datasets import load_dataset

my_dataset = load_dataset("Infatoshi/kernelbench-mega-traces")

# Display dataset details
for example in range(5):  # Display the first 5 examples
    print(my_dataset[example])


#filtered = 
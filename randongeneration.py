# import pandas as pd
# import random
#
# # Generating sample data
# names = ["Arjun Sharma", "Riya Verma", "Mohit Patel", "Sneha Kapoor", "Aditya Rao", "Neha Joshi", "Rajesh Gupta", "Priya Nair",
#          "Vikram Singh", "Ananya Das", "Sameer Khan", "Pooja Roy", "Kunal Mehta", "Kavya Iyer", "Rohan Agarwal", "Meera Sinha",
#          "Suresh Reddy", "Swati Bhatt", "Aman Thakur", "Divya Kulkarni"]
#
# genders = ["Male", "Female"]
# customer_types = ["New", "Old"]
# order_types = ["Prepaid", "Cash on Delivery"]
# cities = ["Mumbai", "Delhi", "Ahmedabad", "Bangalore", "Hyderabad", "Pune", "Kolkata", "Chennai", "Jaipur", "Chandigarh",
#           "Lucknow", "Bhopal", "Surat", "Coimbatore", "Vadodara", "Indore", "Visakhapatnam", "Nagpur", "Patna", "Ludhiana"]
# promotions = ["Purchased with no discount", "Purchased using discount coupon", "Purchased on sale"]
#
# # "Id": [random.choice(names) for _ in range(500)],
# # Create a dataframe
# data = {
#     "Gender": [random.choice(genders) for _ in range(500)],
#     "Age": [random.randint(14, 60) for _ in range(500)],
#     "Customer_Type": [random.choice(customer_types) for _ in range(500)],
#     "Order_Type": [random.choice(order_types) for _ in range(500)],
#     "City": [random.choice(cities) for _ in range(500)],
#     "Affiliation_to_Promotion": [random.choice(promotions) for _ in range(500)],
#     "Spending_score": [random.randint(10, 99) for _ in range(500)]
# }
#
# df = pd.DataFrame(data)
#
# # Save to CSV
# csv_path = "input_data/product_1002_customers.csv"
# df.to_csv(csv_path, index=False)
# csv_path

# import pandas as pd
#
# # Load the Excel file
# file_path = 'input_data/E Commerce Dataset.xlsx'  # replace with your actual file path
# sheet_name = 'E Comm'
#
# # Read the specified sheet
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # Check 'Tenure' column and apply conditions
# df['Status'] = df['Tenure'].apply(lambda x: 'New' if pd.isnull(x) or (0 <= x <= 10) else 'Old')
#
# # Save the modified DataFrame back to an Excel file
# output_file_path = 'input_data/modified_file.xlsx'  # replace with your desired output file path
# df.to_excel(output_file_path, sheet_name=sheet_name, index=False)
#
# print("Process completed. The modified file is saved as", output_file_path)


# import pandas as pd
# import random
#
# # Load the Excel file
# file_path = 'input_data/modified_file.xlsx'  # replace with your actual file path
# sheet_name = 'E Comm'
#
# # Read the specified sheet
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # Check 'Tenure' column and apply conditions
# df['Status'] = df['Tenure'].apply(lambda x: 'New' if pd.isnull(x) or (0 <= x <= 10) else 'Old')
#
# # Comprehensive list of US cities across more than 50 states
# us_cities = [
#     'New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX', 'Phoenix, AZ',
#     'Philadelphia, PA', 'San Antonio, TX', 'San Diego, CA', 'Dallas, TX', 'San Jose, CA',
#     'Austin, TX', 'Jacksonville, FL', 'Fort Worth, TX', 'Columbus, OH', 'San Francisco, CA',
#     'Charlotte, NC', 'Indianapolis, IN', 'Seattle, WA', 'Denver, CO', 'Washington, DC',
#     'Boston, MA', 'El Paso, TX', 'Nashville, TN', 'Detroit, MI', 'Oklahoma City, OK',
#     'Portland, OR', 'Las Vegas, NV', 'Memphis, TN', 'Louisville, KY', 'Baltimore, MD',
#     'Milwaukee, WI', 'Albuquerque, NM', 'Tucson, AZ', 'Fresno, CA', 'Sacramento, CA',
#     'Mesa, AZ', 'Kansas City, MO', 'Atlanta, GA', 'Omaha, NE', 'Colorado Springs, CO',
#     'Raleigh, NC', 'Miami, FL', 'Virginia Beach, VA', 'Oakland, CA', 'Minneapolis, MN',
#     'Tulsa, OK', 'Arlington, TX', 'New Orleans, LA', 'Wichita, KS', 'Cleveland, OH',
#     'Tampa, FL', 'Bakersfield, CA', 'Aurora, CO', 'Anaheim, CA', 'Honolulu, HI',
#     'Santa Ana, CA', 'Riverside, CA', 'Corpus Christi, TX', 'Lexington, KY', 'Henderson, NV',
#     'Stockton, CA', 'Saint Paul, MN', 'Cincinnati, OH', 'St. Louis, MO', 'Pittsburgh, PA',
#     'Greensboro, NC', 'Lincoln, NE', 'Anchorage, AK', 'Plano, TX', 'Orlando, FL',
#     'Irvine, CA', 'Newark, NJ', 'Durham, NC', 'Chula Vista, CA', 'Fort Wayne, IN',
#     'Jersey City, NJ', 'St. Petersburg, FL', 'Laredo, TX', 'Madison, WI', 'Chandler, AZ',
#     'Buffalo, NY', 'Lubbock, TX', 'Scottsdale, AZ', 'Reno, NV', 'Glendale, AZ',
#     'Gilbert, AZ', 'Winston–Salem, NC', 'North Las Vegas, NV', 'Norfolk, VA', 'Chesapeake, VA'
# ]
#
#
# # # Add two new columns 'city1' and 'city2' with random US cities
# # df['city'] = [random.choice(us_cities) for _ in range(len(df))]
# df['spending_score'] = [random.randint(10, 90) for _ in range(len(df))]
# def get_affiliation(x):
#     if pd.isnull(x) or x <= 1:
#         return 'NoCoupon'
#     elif x == 2:
#         return 'InSale'
#     elif x == 3:
#         return 'UsingCoupon'
#     else:
#         return 'Unknown'
#
#
# # Apply the function to create the new column 'AffliationToPromotion'
# df['AffiliationToPromotion'] = df['HourSpendOnApp'].apply(get_affiliation)
#
# # Save the modified DataFrame back to an Excel file
# output_file_path = 'input_data/modified_file.xlsx'  # replace with your desired output file path
# df.to_excel(output_file_path, sheet_name=sheet_name, index=False)
#
# print("Process completed. The modified file is saved as", output_file_path)


import pandas as pd

# Load the modified Excel file
file_path = 'input_data/modified_file.xlsx'  # replace with the actual file path
df = pd.read_excel(file_path)

# Split the data into six parts
split_size = len(df) // 6

# Iterate over each split and save it as a separate file
for i in range(6):
    start_index = i * split_size
    end_index = start_index + split_size if i < 5 else len(df)

    # Extract the split
    split_df = df.iloc[start_index:end_index]

    # Save the split as a new file with the specified name
    output_file_path = 'input_data/' + str(i + 1002) + '.xlsx'
    split_df.to_excel(output_file_path, index=False)
    print(f"Split {i + 1} saved as {output_file_path}")

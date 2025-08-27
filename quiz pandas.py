import pandas as pd

# 0) البيانات من الصورة (مكتوبة داخل الكود)
data = {
    "Transaction_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer_Name": ["Ahmed Ali", "Sara Omar", "Ali Saleh", "Nada Hassan", "Omar Khalid", "Ahmed Ali"],
    "Age": [28, None, 33, 42, None, 28],
    "Email": ["ahmed@mail.com", "sara@mail.com", None, "nada@mail.com", "omar@mail.com", "ahmed@mail.com"],
    "Join_Date": ["2025-01-10", "2025-02-15", "2025-03-20", None, "2025-05-05", "2025-01-10"],
    "Total_Purchase": [250, 300, 150, 400, None, 250]
}

df = pd.DataFrame(data)

print("=== البيانات الأصلية (الجدول قبل التعديلات) ===")
print(df.to_string(index=False))
print("\n")

# 1) تحويل عمود Join_Date إلى تاريخ
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
print("1) بعد تحويل Join_Date إلى تاريخ:")
print(df.to_string(index=False))
print("\n")

# 2) الصفوف التي فيها أكثر من قيمة فارغة
print("2) الصفوف التي فيها أكثر من قيمة فارغة:")
print(df[df.isnull().sum(axis=1) > 1])
print("\n")
# نوع البيانات وعدد الصفوف والاعمدة  -3
print("عدد الصفوف والأعمدة:")
print(f"عدد الصفوف: {df.shape[0]}")
print(f"عدد الأعمدة: {df.shape[1]}")
print("-" * 30)

#  نوع البيانات لكل عمود
print("أنواع البيانات لكل عمود:")
print(df.dtypes)
print("\n")

# 4) عدد القيم الفارغة في كل عمود
print("4) عدد القيم الفارغة في كل عمود:")
print(df.isnull().sum())
print("\n")

# 5) الصفوف التي العمر أقل من 30
print("5) الصفوف التي العمر فيها أقل من 30:")
print(df[df["Age"] < 30])
print("\n")

# 6) كم صف يتبقى بعد حذف الصفوف اللي فيها أي قيمة فارغة
print("6) عدد الصفوف المتبقية بعد حذف أي صف فيه قيم فارغة:")
print(df.dropna().shape[0])
print("\n")

# 7) استبدال القيم الفارغة في Age بالمتوسط
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("7) بعد استبدال القيم الفارغة في Age بالمتوسط:")
print(df.to_string(index=False))
print("\n")

# 8) استبدال القيم الفارغة في Total_Purchase بالرقم 0
df["Total_Purchase"] = df["Total_Purchase"].fillna(0)
print("8) بعد استبدال القيم الفارغة في Total_Purchase بالرقم 0:")
print(df.to_string(index=False))
print("\n")

# 9) معرفة الصفوف المكررة قبل الحذف
print("9) الصفوف المكررة قبل الحذف:")
duplicates = df[df.duplicated()]
print(duplicates.to_string(index=False))
print("\n")

# 10) إزالة الصفوف المكررة
df = df.drop_duplicates()
print("10) بعد إزالة الصفوف المكررة:")
print(df.to_string(index=False))
print("\n")

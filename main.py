from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
predicted_model = joblib.load('./models/prediction2.joblib')
app = FastAPI()
class Customers(BaseModel):
    AccountWeeks: float
    ContractRenewal: int
    DataPlan: int
    DataUsage: float
    CustServCalls: int
    DayMins: float
    DayCalls: int
    MonthlyCharge: float
    OverageFee: float
    RoamMins: float
   


@app.get("/home")
def home():
    print("My name is Manish Khadka")
    return {"response":"200", "message":"Success"}
class Employee(BaseModel):
    name: str
    age: int
    salary: float

@app.post("/insert")
def insert(data: Employee):
    print(f"{data.name}\n{data.age}\n{data.salary}")
    return {"response":"200", "message":"Success"}

@app.post("/predict")
def model_predict(data:Customers):
    data = [[
        data.AccountWeeks, data.ContractRenewal, data.DataPlan,
        data.DataUsage, data.CustServCalls, data.DayMins,
        data.DayCalls, data.MonthlyCharge, data.OverageFee,
        data.RoamMins
    ]]
    prediction = predicted_model.predict(data)

    if prediction[0] == 1:
        return "Customer will churn"
    else:
        return "Customer will not churn"


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8084, reload=True)

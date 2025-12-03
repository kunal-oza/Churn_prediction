from pydantic import BaseModel, Field
from typing import Literal, Annotated


class InputData(BaseModel):
    CustomerID: Annotated[int, Field(...)]
    gender: Annotated[Literal['Male', 'Female'], Field(...)]
    SeniorCitizen: Annotated[Literal[1, 0], Field(...)]
    Partner: Annotated[Literal['Yes', 'No'], Field(...)]
    Dependents: Annotated[Literal['Yes', 'No'], Field(...)]
    tenure: Annotated[int, Field(..., ge=0, le=72)]
    PhoneService: Annotated[Literal['Yes', 'No'], Field(...)]
    MultipleLines: Annotated[Literal['Yes', 'No', 'No phone service'], Field(...)]
    InternetService: Annotated[Literal['DSL', 'Fiber optic', 'No'], Field(...)]
    OnlineSecurity: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]
    OnlineBackup: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]
    DeviceProtection: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]
    TechSupport: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]
    StreamingTV: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]
    StreamingMovies: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...)]

    Contract: Annotated[
        Literal['Month-to-month', 'One year', 'Two year'], Field(...)
    ]

    PaperlessBilling: Annotated[Literal['Yes', 'No'], Field(...)]
    PaymentMethod: Annotated[
        Literal[
            'Electronic check',
            'Mailed check',
            'Bank transfer (automatic)',
            'Credit card (automatic)'
        ],
        Field(...)
    ]

    MonthlyCharges: Annotated[float, Field(..., ge=0)]
    total_charges: Annotated[float, Field(..., ge=0)]

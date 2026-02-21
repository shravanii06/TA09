# System Design 

## 1. Technology  Stack 

### Fronted
- React.js (Interactive Dashboard UI)
- Tailwind CSS (Responsive Design)
- Chart.js / Recharts (Data Visulization)
- Leaflet.js (Geospatial Risk Mapping)

### Backend 
- FastAPI (python based REST APIs)
- Uvicorn (ASGI server)
- JWT Authentication (secure access control)

### Database 
- POstgreSQL (structure relational DATA)
- PostGIS (Geospactial queries support)

### Machine Learning
- XGBoost (Outbreak risk prediction)
- LSTM (time series environ. analysis)
- Scikit-learn ( data preprocessing & validation)

## 2. System Components 

### A. Data Ingstion Service
- Fetches satallite and environmental datasets
- Handles API based 
- Stores raw data in database 

### B. Risk Prediction Engine 
- Preprocesses environmental indicators
- Generates outbreak probability score 
- Classifies locality risk (Low / medium / high)

### C. Funding Automation Module
- Moniters risks threshlod values 
- triggers smart contract execution 
- logs transaction details in blockchain

### D. supply recommendation engine 
- maps predicted disease = required medical supplies 
- generates inventory recommandation for clinics

### E. Dashboard Interface
- display risk heatmaps 
- shows funding release status 
- provides alerts & analytics to administrator 

## 3. Data FLow (Technical)

1. Environment data stored in postgreSQL
2. ML model fetches procesed dataset
3. risk scrore generated
4. databoard updates in real time via APi polling

## 4. Scalability & Security 

- Modules microservices ready architecture  
- API rate limiting 
- role based authentication 
- blockcahin based immute transaction records 
- clouds deployalable 


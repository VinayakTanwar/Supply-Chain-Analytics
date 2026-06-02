# Supply Chain Performance & Logistics Analytics Pipeline 

Hey everyone! This is my end-to-end data project. I took a massive supply chain dataset (over 35,000 rows), cleaned it up entirely using **Python**, built an automated secure pipeline to stream it into a **MySQL database**, and then designed a premium, Apple-inspired dark-mode dashboard in **Power BI** to see where the business is losing money and tracking shipment delays.

---

###  Dashboard Preview

> <img width="1239" height="679" alt="Screenshot 2026-06-02 145313" src="https://github.com/user-attachments/assets/842bda96-9815-4c7d-b9cc-337ae9fc68aa" />
---

###  What Was the Problem?
The original data was super messy with weird characters, blank spaces, and terrible column headers. It also had massive outlier data points (like profit margins dropping below -240%) which completely warped the company's real operational averages. If a regular business manager tried to look at the raw data, they wouldn't understand a thing.

###  What I Did (Step-by-Step)

#### 1. The Python Clean Up & ETL Pipeline (`/Scripts/`)
* Used **Pandas** and **NumPy** to fix column headers (replacing spaces and symbols with clean underscores), strip empty trailing spaces, and normalize text data.
* Handled major financial outliers by capping unrealistic profit loss margins so the final chart values wouldn't look broken.
* Built a smart database loop using **SQLAlchemy** and `types` that automatically reads the data frames, infers the column data types, and creates optimal tables in my local MySQL server automatically.
* **Security First:** Kept all local MySQL root database passwords completely hidden from the public repo by utilizing a `.env` environment variable file paired with a `.gitignore` script.

#### 2. The Power BI Bento Dashboard (`/Dashboard/`)
* Instead of making a boring default software report, I styled the entire interface into a modern **Bento Grid layout** (similar to the clean UI style seen in iOS and macOS).
* Used a sleek, deep matte charcoal theme accented by sharp **electric cyan** and **neon violet** data layers to achieve a premium executive look.

---

###  Real Project Insights 

* **Overall Business Health:** The company brought in **$6.47M in Total Revenue** with **$1.44M in Total Profit**, holding a solid **22.27% Profit Margin**. 
* **The Shipping Nightmare:** The single biggest red flag is the **On-Time Delivery Rate, which is sitting at just 18%**. This means a massive **82% of all shipments are facing some kind of delay** (with over 50% flagged explicitly as a Major Delay). 
* **Where the Cash Leaks:** Looking at the *Average Shipping Delay by Region*, regions like the **South of USA** and **South Asia** consistently hit the highest delay peaks. Logistics managers need to optimize carrier partnerships in these zones immediately.
* **Top Profit Drivers:** The **"Cleats"** and **"Camping & Hiking"** categories are completely carrying the company's financial success, driving both the highest total sales volume and overall profitability.

---

###  Repository File Structure

* **`/Dashboard/`**: Contains the master `supply chain dashboard.pbit` file along with a high-res `supply chain dashboard.pdf` copy for instant browser viewing.
* **`/Dataset/`**: Holds the cleaned supply chain transaction data file.
* **`/Scripts/`**: 
  * `supplychainDA.ipynb`: The Jupyter Notebook containing my exploratory testing and cleaning phase.
  * `supplychainETL.py`: The final automated, production-ready Python pipeline script.
  * `.gitignore`: Built to keep the local configuration environment files hidden.
* **`README.md`**: The document you are reading right now!

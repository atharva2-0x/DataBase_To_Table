import sqlite3

conn = sqlite3.connect('demo_database.db')


cur = conn.cursor()



cur.execute('''
CREATE TABLE IF NOT EXISTS consumers (
    consumer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email_address TEXT NOT NULL,
    account_number TEXT NOT NULL,
    meter_number TEXT NOT NULL,
    tariff_plan TEXT NOT NULL,
    consumption_history TEXT NOT NULL,
    payment_status TEXT NOT NULL
)
''')



demo_data = [
    (1, 'Atharva Swami', 'new colony, near hospital, latur, maharashatra, 413521', '9421545555', 'Atharva.Swami@example.com', '123456789', '1234567890123456789', 'Standard', '[100, 200, 300]', 'Paid'),
    (2, 'Alice Deshpande', 'Main St, new hospital, Pune, mh, 411055', '94215545556', 'Alice.Deshpande@example.com', '234567890', '234567890123456789', 'Standard', '[150, 250, 350]', 'Unpaid'),
    (3, 'Deva pandu', 'sector 26, pradhikaran, pune, mh, 411044', '94555455557', 'Deva.pandu@example.com', '345678901', '34567890123456789', 'Premium', '[200, 300, 400]', 'Paid')
]

cur.executemany('''
INSERT INTO consumers (
    consumer_id,
    name,
    address,
    contact_number,
    email_address,
    account_number,
    meter_number,
    tariff_plan,
    consumption_history,
    payment_status
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', demo_data)


conn.commit()
conn.close()
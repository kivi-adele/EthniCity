from flask import Flask, request, jsonify
import sqlite3
from openai import OpenAI
client = OpenAI(api_key='')

app = Flask(__name__)

# Set up your OpenAI API key

def connect_db():
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        # Handle the error appropriately (e.g., return None or exit)


def generate_customs(festival_name):
  client = OpenAI(
      api_key="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",
  )

  prompt = f"Generate traditional customs for the festival {festival_name}."

  response = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="gpt-4",
  )

  # Rest of the code for processing the response remains the same
  customs_text = response.choices[0].message.content.strip()
  customs_list = customs_text.split('\n')
  return [custom.strip() for custom in customs_list if custom.strip()]




@app.route('/add_festival_with_customs', methods=['POST'])
def add_festival_with_customs():
    data = request.json
    festival_name = data['name']
    festival_date = data['date']

    # Generate customs using GPT-3
    customs = generate_customs(festival_name)

    # Insert festival into database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Festivals (name, date) VALUES (?, ?)", (festival_name, festival_date))
    festival_id = cursor.lastrowid

    # Insert customs into database
    for custom in customs:
        cursor.execute("INSERT INTO Customs (festival_id, description) VALUES (?, ?)", (festival_id, custom))

    conn.commit()
    conn.close()

    return jsonify({'festival_id': festival_id, 'name': festival_name, 'date': festival_date, 'customs': customs}), 201

if __name__ == '__main__':
    app.run(debug=True)
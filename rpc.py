from pypresence import Presence
import time

client_id = "YOUR_CLIENT_ID"  # Replace with your actual client ID
RPC = Presence(client_id)

RPC.connect()
print("RPC is ready")  # Print statement indicating that RPC is ready

RPC.update(state="Check Out My Social Media",
           large_image="icon",
           buttons=[{
             "label": "My Social Media",
             "url": "https://example.com/button"
           }, {
             "label": "Button 2",
             "url": "https://example.com/button2"
           }])

while True:
  time.sleep(60)


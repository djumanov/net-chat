# Net-Chat

Net-Chat is a desktop messaging application designed for employees to communicate with each other over a local network. This project uses **WebSockets**, **PyQt5**, and **PostgreSQL** for real-time communication and data storage.

## Features

- Real-time messaging between employees on the same local network.
- User-friendly GUI built with PyQt5.
- Communication via WebSockets for real-time message exchange.
- Messages and user information are stored in PostgreSQL.

## Technology Stack

- **Python**: Core programming language.
- **WebSockets**: Enables real-time communication between the client and server.
- **PyQt5**: Provides the graphical interface for desktop users.
- **PostgreSQL**: Relational database for storing user data and messages.
- **asyncio**: Manages asynchronous tasks for non-blocking WebSocket connections.

## Installation

### Requirements

Ensure the following are installed on your system:

- Python 3.8+
- PostgreSQL
- Required Python libraries (`websockets`, `asyncpg`, `PyQt5`)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/net-chat.git
   cd net-chat
   ```

2. **Install dependencies**:
   ```bash
   pip install websockets asyncpg PyQt5
   ```

3. **Set up PostgreSQL database**:
   - Create a PostgreSQL database:
     ```sql
     CREATE DATABASE netchat;
     ```
   - Create the necessary tables:
     ```sql
     CREATE TABLE users (
         id SERIAL PRIMARY KEY,
         name VARCHAR(100),
         status VARCHAR(10)
     );

     CREATE TABLE messages (
         id SERIAL PRIMARY KEY,
         sender_id INTEGER REFERENCES users(id),
         receiver_id INTEGER REFERENCES users(id),
         message TEXT,
         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. **Configure database settings**:
   - Edit the `server.py` file and update the PostgreSQL connection details with your credentials:
     ```python
     async def init_db():
         return await asyncpg.connect(
             user='your_username', 
             password='your_password', 
             database='netchat', 
             host='localhost'
         )
     ```

5. **Run the WebSocket server**:
   ```bash
   python server.py
   ```

6. **Run the PyQt5 client**:
   - Create your client-side application in PyQt5, connect it to the WebSocket server, and launch it.

## Usage

Once both the server and client applications are running, users can connect to the local network and start sending real-time messages to each other. Messages are stored in the PostgreSQL database for future reference.

### Server

The WebSocket server handles connections from multiple clients, routing messages between them. It also stores all messages in the PostgreSQL database.

### Client

The PyQt5 client allows users to log in, send messages, and receive real-time messages from others. The client communicates with the WebSocket server.

## Future Enhancements

- User authentication system (login/registration).
- Message encryption for added security.
- File sharing capabilities.
- Offline message delivery when a user reconnects.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

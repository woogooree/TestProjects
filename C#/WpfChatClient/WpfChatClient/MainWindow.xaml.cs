using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfChatClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private Socket clientSocket;
        private Thread receiveThread;

        public MainWindow()
        {
            InitializeComponent();
            ConnectToServer();
        }

        private void ConnectToServer()
        {
            clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            clientSocket.Connect(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8080));
            receiveThread = new Thread(ReceiveMessages);
            receiveThread.Start();
        }

        private void ReceiveMessages()
        {
            byte[] buffer = new byte[1024];
            int received;

            while (true)
            {
                try
                {
                    received = clientSocket.Receive(buffer);
                    if (received == 0) break;

                    string response = Encoding.ASCII.GetString(buffer, 0, received);
                    Dispatcher.Invoke(() => ChatTextBox.AppendText("Server: " + response + "\n"));
                }
                catch
                {
                    Dispatcher.Invoke(() => ChatTextBox.AppendText("Disconnected from server\n"));
                    break;
                }
            }

            clientSocket.Close();
        }

        private void SendButton_Click(object sender, RoutedEventArgs e)
        {
            SendMessage();
        }

        private void MessageTextBox_KeyDown(object sender, System.Windows.Input.KeyEventArgs e)
        {
            if (e.Key == System.Windows.Input.Key.Enter)
            {
                SendMessage();
            }
        }

        private void SendMessage()
        {
            string message = MessageTextBox.Text;
            if (!string.IsNullOrEmpty(message))
            {
                byte[] data = Encoding.ASCII.GetBytes(message);
                clientSocket.Send(data);
                ChatTextBox.AppendText("Client: " + message + "\n");
                MessageTextBox.Clear();
            }
        }
    }
}
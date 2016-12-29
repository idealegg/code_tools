import paramiko


class MySshClient:
    def __init__(self, private_key_file, host_key_file, host_name, user_name, port=22):
        self._client = None
        self._private_key_file = private_key_file
        self._host_key_file = host_key_file
        self._host_name = host_name
        self._port = port
        self._user_name = user_name
        self._key = None
        self._std_in = None
        self._std_out = None
        self._std_err = None

    def initialize(self):
        self._key = paramiko.RSAKey.from_private_key_file(self._private_key_file)
        self._client = paramiko.SSHClient()
        self._client.load_system_host_keys()

        self._client.load_system_host_keys(self._host_name)
        self._client.connect(self._host_name, self._port, self._user_name, pkey=self._key)

    def exec_command(self, cmd):
        std_in, std_out, std_err = self._client.exec_command(cmd)
        self._std_in = std_in.read()
        self._std_out = std_out.read()
        self._std_err = std_err.read()
        return self._std_in, self._std_out, self._std_err

    def close(self):
        self._client.close()



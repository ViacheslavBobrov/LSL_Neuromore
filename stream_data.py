from pylsl import StreamInlet, resolve_byprop
from pythonosc import udp_client
from threading import Thread
from time import sleep


class MuseLslToOscStreamer:

    def __init__(self, host, port):
        self.client = udp_client.SimpleUDPClient(host, port)
        self.inlet = None
        self.stream_channels = [
            "/muse/tp9",
            "/muse/af7",
            "/muse/af8",
            "/muse/tp10",
            "/muse/aux"
        ]
        self.is_streaming = False

    def connect(self):
        streams = resolve_byprop('type', 'EEG', timeout=5)
        self.inlet = StreamInlet(streams[0], max_chunklen=12)
        return self.inlet is not None

    def stream_data(self):
        if self.inlet is None:
            raise Exception("Muse lsl stream is not connected")
        self.is_streaming = True
        streaming_thread = Thread(target=self._stream_handler)
        streaming_thread.setDaemon(True)
        streaming_thread.start()

    def _stream_handler(self):
        while self.is_streaming:
            eeg_sample, _ = self.inlet.pull_sample()
            for channel_idx, channel in enumerate(self.stream_channels):
                self.client.send_message(channel, eeg_sample[channel_idx])

    def close_stream(self):
        self.is_streaming = False
        self.inlet.close_stream()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4545
    stream_time_sec = 3600

    streamer = MuseLslToOscStreamer(host, port)
    streamer.connect()

    print("Start streaming data to {}:{} for {} seconds".format(host, port, stream_time_sec))
    streamer.stream_data()
    sleep(stream_time_sec)
    streamer.close_stream()
    print("Stopped streaming. Exiting program...")

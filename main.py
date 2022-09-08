# pip install speedtest-cli
import speedtest


def test_my_speed():
    test = speedtest.Speedtest()
    test.get_servers()  # get server
    print("Choosing best server...")
    best_server = test.get_best_server()
    print("Server chosen!" + f"{best_server}")
    print("Now lets find out the download and upload speed!")
    download_speed = test.download() / 1024 /1024
    upload_speed = test.upload() / 1024 / 1024
    # {:.2f} {:+.2f} 这些都是str.format()格式化数字的方法
    print("OK, the download speed is " + f"{download_speed:.2f}"+
          " mb, and the upload speed is " + f"{upload_speed:.2f}"+ " mb")
    ping = test.results.ping
    print("The ping is " + f"{ping:.0f}" + " ms")


if __name__ == '__main__':
    test_my_speed()
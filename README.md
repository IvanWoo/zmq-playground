# zmq-playground

## prerequisites

- [pdm](https://github.com/pdm-project/pdm): `2.2.1`
- [Wireshark](https://www.wireshark.org) `4.0.1`
  - `brew install --cask wireshark`

## setup

### python

```sh
pdm install
```

### install [ZMTP Wireshark Dissector](https://github.com/whitequark/zmtp-wireshark)

```sh
mkdir -p ~/.config/wireshark/plugins
git clone https://github.com/whitequark/zmtp-wireshark.git ~/.config/wireshark/plugins/zmtp-wireshark
```

## sniff the packets

start wireshark and capture your loopback

send some messages over the wire

```sh
pdm run python server.py
pdm run python client.py
```

decode the tcp packets as zmtp

![where is decode as](./assets/where_is_decode_as.png)

![decode as modal](./asserts/../assets/decode_as_modal.png)

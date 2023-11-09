from struct import unpack as convert

encode = bytes.fromhex
hex_to_double = lambda hex: convert('!d', encode(hex))[0]

print(hex_to_double('bfaa4ee27cf1198d'))

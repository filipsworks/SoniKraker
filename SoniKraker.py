def CRC16(crc, buffer):
    for _ in range(len(buffer)):
        crc ^= buffer.pop(0) << 8
        bits = 0
        while bits < 8:
            if (crc & 0x8000) != 0:
                crc = (2 * crc) ^ 0x1021
            else:
                crc *= 2
            bits += 1
    return crc


nfctag_uid = bytearray.fromhex(input("Input UID: "))
nfc_mfg = input("Input MFG: ").encode('ascii')

pwd = CRC16(0x49A3, nfctag_uid.copy())
pwd = pwd | (CRC16(pwd, list(nfc_mfg)) << 16)
pwd = (crc_calc >> 8) & 0x00FF00FF | (crc_calc << 8) & 0xFF00FF00

print(f"NFC PWD: 0x{crc_calc:08X}")

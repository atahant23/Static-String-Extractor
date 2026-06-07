import zipfile
import os
import hashlib

def calculate_file_hashes(file_path):
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        return {
            "size": f"{os.path.getsize(file_path) / 1024:.2f} KB",
            "md5": md5_hash.hexdigest(),
            "sha256": sha256_hash.hexdigest()
        }
    except Exception:
        return {"size": "0 KB", "md5": "N/A", "sha256": "N/A"}

def detect_file_format(file_path):
    try:
        with open(file_path, 'rb') as f:
            magic = f.read(4)
        if magic.startswith(b'\x7fELF'):
            return "Linux Executable (ELF Linkable format)"
        elif magic.startswith(b'MZ'):
            return "Windows Executable (PE Portable Executable)"
        elif magic.startswith(b'PK\x03\x04'):
            return "Symmetric Compressed Archive (APK / ZIP Package)"
        else:
            return "Unknown Raw Binary Stream"
    except Exception:
        return "Unresolved File Architecture"

def parse_bytes(payload, min_length):
    extracted_strings = []
    temporary_buffer = []
    for byte_value in payload:
        if 32 <= byte_value <= 126:
            temporary_buffer.append(chr(byte_value))
        else:
            if len(temporary_buffer) >= min_length:
                extracted_strings.append("".join(temporary_buffer))
            temporary_buffer = []
    if len(temporary_buffer) >= min_length:
        extracted_strings.append("".join(temporary_buffer))
    return extracted_strings

def extract_strings(file_path, min_length=4):
    extracted_strings = []
    file_format = detect_file_format(file_path)
    metadata = calculate_file_hashes(file_path)
    try:
        if file_path.endswith('.apk') or file_path.endswith('.zip') or file_format.startswith("Symmetric"):
            with zipfile.ZipFile(file_path, 'r') as archive:
                for file_info in archive.infolist():
                    try:
                        with archive.open(file_info) as archived_file:
                            file_payload = archived_file.read()
                            extracted_strings.extend(parse_bytes(file_payload, min_length))
                    except Exception:
                        pass
        else:
            with open(file_path, 'rb') as binary_stream:
                raw_payload = binary_stream.read()
            extracted_strings.extend(parse_bytes(raw_payload, min_length))
    except Exception:
        pass
    return list(set(extracted_strings)), file_format, metadata

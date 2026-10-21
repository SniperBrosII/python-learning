print("Problem 1: Security Log Splitter and Status Report")
def split_logs(machines):
    counts = {}
    with open("info.log", "w") as info_file, \
        open("warning.log", "w") as warning_file, \
        open("error.log", "w") as error_file:
            output_files = {
                "INFO": info_file,
                "WARNING": warning_file,
                "ERROR": error_file
            }
            for machine, filename in machines.items():
                counts[machine] = {
                    "INFO": 0,
                    "WARNING": 0,
                    "ERROR": 0
                }
                with open(filename, "r") as input_file:
                    for line in input_file:
                        line = line.rstrip("\n")
                        if not line.strip():
                            continue
                        if "[INFO]" in line:
                            level = "INFO"
                        elif "[WARNING]" in line:
                            level = "WARNING"
                        elif "[ERROR]" in line:
                            level = "ERROR"
                        else:
                            continue
                        output_files[level].write(
                            machine + " | " + line + "\n"
                        )
                        counts[machine][level] += 1
    return counts
def print_report(counts, error_file="error.log"):
    print("=" * 40)
    print("SECURITY LOG STATUS REPORT")
    print("=" * 40)
    total_info = 0
    total_warning = 0
    total_error = 0
    for machine, levels in counts.items():
        info = levels["INFO"]
        warning = levels["WARNING"]
        error = levels["ERROR"]
        total = info + warning + error
        total_info += info
        total_warning += warning
        total_error += error
        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        print(
            f"{machine}: {total} entries | "
            f"INFO: {info} | WARNING: {warning} | "
            f"ERROR: {error} | Status: {status}"
        )
    print("-" * 40)
    total_entries = total_info + total_warning + total_error
    print(
        f"TOTAL: {total_entries} entries | "
        f"INFO: {total_info} | WARNING: {total_warning} | "
        f"ERROR: {total_error}"
    )
    print("-" * 40)
    print("ERROR LOG")
    print("-" * 40)
    with open(error_file, "r") as file:
        for line in file:
            print("  " + line.rstrip("\n"))
    print("=" * 40)
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")
with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")
counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)
with open("warning.log", "r") as f:
    print(f.read())
print_report(counts)
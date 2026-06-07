import json
import os

def save_report(data, output_dir, filename="report.json"):
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, filename)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return report_path

def save_html_report(data, file_format, metadata, target_name, output_dir, filename="report.html"):
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, filename)
    
    alerts_html = ""
    for alert in data["High_Risk_Alerts"]:
        alerts_html += f"""
        <li class='list-group-item d-flex justify-content-between align-items-center text-white border-secondary' style='background-color: #3b1111; border-color: #551a1a !important; margin-bottom: 6px; border-radius: 6px;'>
            <code style='color: #fca5a5 !important; font-weight: bold; font-size: 1.05rem;'>{alert['string']}</code>
            <span class='badge bg-danger text-white px-3 py-2'>Entropy: {alert['entropy']}</span>
        </li>"""
        
    if not alerts_html:
        alerts_html = "<li class='list-group-item border-secondary' style='background-color: #14532d; color: #4ade80;'>No high-risk security anomalies or structural leaks identified in the surface layer.</li>"

    capabilities_html = ""
    for cap in data["Suspicious_Capabilities_Or_APIs"]:
        capabilities_html += f"""
        <div class='m-2 p-3 rounded text-start shadow-sm' style='background-color: #1e293b; border: 1px solid #374151; min-width: 280px; flex: 1;'>
            <h5 style='color: #fbbf24; font-weight: bold; margin-bottom: 6px;'>⚡ {cap['string'].upper()}</h5>
            <small style='color: #cbd5e1; display: block; white-space: normal; word-break: break-all;'>Found in: {cap['context']}</small>
        </div>"""
    if not capabilities_html:
        capabilities_html = "<p style='color: #94a3b8; padding-left: 8px;'>No suspect binary capability vectors mapped from predefined rulesets.</p>"

    general_strings_html = ""
    for idx, gs in enumerate(data["General_Strings"][:200]):
        general_strings_html += f"<tr><td style='color: #94a3b8;'>{idx+1}</td><td style='color: #38bdf8; font-family: monospace; word-break: break-all;'>{gs['string']}</td><td style='color: #64748b;'>{gs['entropy']}</td></tr>"

    html_content = f"""<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <title>Advanced Static Binary Analysis Platform</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
        <style>
            body {{ background-color: #090d16; color: #f1f5f9; font-family: 'Segoe UI', system-ui, sans-serif; }}
            .card-custom {{ background-color: #111827; border: 1px solid #1f2937; border-radius: 12px; }}
            .metric-card {{ background-color: #111827; border: 1px solid #1f2937; border-radius: 10px; }}
            .table-custom {{ background-color: #111827 !important; color: #f1f5f9 !important; }}
            .table-custom th {{ background-color: #1f2937 !important; color: #ffffff !important; border-bottom: 2px solid #374151 !important; }}
            .table-custom td {{ border-bottom: 1px solid #1f2937 !important; }}
            .scroll-box {{ max-height: 400px; overflow-y: auto; border: 1px solid #1f2937; border-radius: 8px; }}
        </style>
    </head>
    <body class='p-5'>
        <div class='container-fluid px-md-5'>
            <div class='p-4 mb-4 card-custom shadow-lg'>
                <div class='d-flex justify-content-between align-items-center flex-wrap mb-4'>
                    <div>
                        <h1 class='display-5 fw-bold mb-1' style='color: #4ade80 !important;'>Advanced Static Analysis Dashboard</h1>
                        <p class='fs-6 mb-0' style='color: #94a3b8 !important;'>Automated Reverse Engineering & Threat Intelligence Engine</p>
                    </div>
                    <span class='badge bg-success text-dark px-3 py-2 fw-bold fs-6 mt-2 mt-md-0'>STATUS: SECURE AUDIT COMPLETE</span>
                </div>
                
                <div class='p-4 rounded shadow-sm' style='background-color: #1f2937; border: 1px solid #374151;'>
                    <h4 style='color: #38bdf8 !important; font-weight: bold; margin-bottom: 20px; border-bottom: 1px solid #374151; padding-bottom: 10px;'>Target Matrix Evaluation Summary</h4>
                    <div class='row g-4 fs-6'>
                        <div class='col-md-6'><span style='color: #4ade80 !important; font-weight: bold;'>Target File:</span><span style='color: #ffffff !important; font-family: monospace; margin-left: 10px; font-weight: 500;'>{target_name}</span></div>
                        <div class='col-md-6'><span style='color: #4ade80 !important; font-weight: bold;'>Substrate Architecture:</span><span style='color: #ffffff !important; margin-left: 10px; font-weight: 500;'>{file_format}</span></div>
                        <div class='col-md-6'><span style='color: #4ade80 !important; font-weight: bold;'>File Size Matrix:</span><span style='color: #ffffff !important; margin-left: 10px; font-weight: 500;'>{metadata['size']}</span></div>
                        <div class='col-md-6'><span style='color: #4ade80 !important; font-weight: bold;'>MD5 Cryptographic Hash:</span><span style='color: #38bdf8 !important; font-family: monospace; margin-left: 10px;'>{metadata['md5']}</span></div>
                        <div class='col-md-12'><span style='color: #4ade80 !important; font-weight: bold;'>SHA256 Fingerprint:</span><span style='color: #38bdf8 !important; font-family: monospace; margin-left: 10px;'>{metadata['sha256']}</span></div>
                    </div>
                </div>
            </div>
            
            <div class='row g-3 mb-4 text-center'>
                <div class='col'><div class='metric-card p-3 shadow-sm'><h2 style='color: #38bdf8 !important; font-weight: bold; margin-bottom: 2px;'>{len(data["URL"])}</h2><span style='color: #94a3b8; font-size: 0.75rem; font-weight: bold;'>EXTRACTED URLS</span></div></div>
                <div class='col'><div class='metric-card p-3 shadow-sm'><h2 style='color: #fbbf24 !important; font-weight: bold; margin-bottom: 2px;'>{len(data["IP_Address"])}</h2><span style='color: #94a3b8; font-size: 0.75rem; font-weight: bold;'>DETECTED IPS</span></div></div>
                <div class='col'><div class='metric-card p-3 shadow-sm'><h2 style='color: #60a5fa !important; font-weight: bold; margin-bottom: 2px;'>{len(data["Email"])}</h2><span style='color: #94a3b8; font-size: 0.75rem; font-weight: bold;'>EMAIL ENTITIES</span></div></div>
                <div class='col'><div class='metric-card p-3 shadow-sm'><h2 style='color: #a78bfa !important; font-weight: bold; margin-bottom: 2px;'>{len(data["Suspicious_Capabilities_Or_APIs"])}</h2><span style='color: #94a3b8; font-size: 0.75rem; font-weight: bold;'>SUSPICIOUS APIS</span></div></div>
                <div class='col'><div class='metric-card p-3 shadow-sm'><h2 style='color: #f87171 !important; font-weight: bold; margin-bottom: 2px;'>{len(data["High_Risk_Alerts"])}</h2><span style='color: #94a3b8; font-size: 0.75rem; font-weight: bold;'>CRITICAL ALERTS</span></div></div>
            </div>
            
            <div class='card-custom p-4 mb-4 shadow-lg'>
                <h3 style='color: #fbbf24 !important; font-weight: bold;' class='mb-3'>Heuristic Behavioral Capabilities</h3>
                <div class='d-flex flex-wrap g-2'>{capabilities_html}</div>
            </div>
            
            <div class='card-custom p-4 mb-4 shadow-lg'>
                <h3 style='color: #f87171 !important; font-weight: bold;' class='mb-3'>High Risk Security Anomalies (Shannon Entropy Threshold Exceeded)</h3>
                <ul class='list-group shadow-sm border-0'>{alerts_html}</ul>
            </div>

            <div class='card-custom p-4 shadow-lg'>
                <h3 style='color: #38bdf8 !important; font-weight: bold;' class='mb-3'>Extracted Binary Strings Buffer Dump (Top 200 Index)</h3>
                <div class='scroll-box'>
                    <table class='table table-custom table-hover mb-0 align-middle'>
                        <thead>
                            <tr><th style='width: 80px; color: #ffffff !important;'>#</th><th style='color: #ffffff !important;'>Extracted Printable Character Sequence</th><th style='width: 150px; color: #ffffff !important;'>Shannon Score</th></tr>
                        </thead>
                        <tbody>{general_strings_html}</tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>"""
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return html_path

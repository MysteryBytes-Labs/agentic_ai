<!-- Enable WSL -->
<tr>
    <td style="padding:12px; width:25%; vertical-align:top;"><strong>3.1 Enable WSL2</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <ol>
            <li>Open PowerShell as Administrator.</li>
            <li>Run:<br>
                <pre><code>wsl --install</code></pre>
            </li>
            <li>Restart your system when prompted.</li>
            <li>By default, Ubuntu will be installed. You can switch distros later if needed.</li>
        </ol>
    </td>
</tr>

<!-- Install Ollama -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>3.2 Install Ollama (inside WSL2)</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <ol>
            <li>Open Ubuntu (WSL2) from the Start Menu.</li>
            <li>Install Ollama using the official script:<br>
                <pre><code>curl -fsSL https://ollama.ai/install.sh | sh</code></pre>
            </li>
            <li>Start the service:<br>
                <pre><code>sudo systemctl enable ollama</code></pre></li>
                </ol>
                </td>
                </tr>
<!-- Verify -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>3.3 Verify Server & Run a Model</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <ol>
            <li>In your browser, visit <code>http://localhost:11434/</code> — you should see “Ollama is running”.</li>
            <li>Test a model:<br>
                <pre><code>ollama run llama3.2</code></pre>
            </li>
        </ol>
    </td>
</tr>

<!-- Requirements -->
<tr>
    <td colspan="2" style="padding:12px;">
        <h3 style="color:#00bfff;">Confirm OS:</h3>
        <span style="color:#00bfff;">
            • Windows 10 22H2+ or Windows 11<br>
            • WSL2 enabled (required for Linux‑based Ollama)<br><br>
        </span>
        <h3 style="color:#00bfff;">Hardware (recommended baseline):</h3>
        <span style="color:#00bfff;">
            • 16 GB RAM or more<br>
            • SSD with 12+ GB free<br>
            • 4–8 CPU cores<br><br>
        </span>
        <h3 style="color:#00bfff;">Developer Tools (optional):</h3>
        <span style="color:#00bfff;">
            • Git, Python, Node.js<br>
            • Windows Terminal<br>
            • Docker Desktop (if composing services)<br>
        </span>
    </td>
</tr>

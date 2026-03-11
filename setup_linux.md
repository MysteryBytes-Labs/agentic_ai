<!-- Update system -->
<tr>
    <td style="padding:12px; width:25%; vertical-align:top;"><strong>4.1 Update System Packages</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <pre><code>sudo apt update && sudo apt upgrade -y</code></pre>
    </td>
</tr>

<!-- Install Ollama -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>4.2 Install Ollama</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <ol>
            <li>Run the official install script:<br>
                <pre><code>curl -fsSL https://ollama.ai/install.sh | sh</code></pre>
            </li>
            <li>Enable and start the service:<br>
                <pre><code>sudo systemctl enable ollama
</code></pre></li>
<li>Api will be available at <pre><code>http://localhost:11434.</code></pre></li>
</ol></td></tr>
<!-- Verify -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>4.3 Verify Server & Run a Model</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <ol>
            <li>Open a browser and visit <code>http://localhost:11434/</code>.</li>
            <li>Run a model:<br>
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
            • Ubuntu 22.04+ (recommended)<br>
            • Debian, Fedora, Arch, and other modern 64‑bit distros also supported<br><br>
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
            • Docker (for multi‑service setups)<br>
        </span>
    </td>
</tr>

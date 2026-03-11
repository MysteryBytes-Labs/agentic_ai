<!-- System Requirements -->
<tr>
<td style="padding:12px; width:25%; vertical-align:top;"><strong>1.1 System Requirements</strong></td>
    <td style="padding:12px; vertical-align:top;">
        <h3 style="color:#00bfff;">Confirm OS:</h3>
        <span style="color:#00bfff;">
            • macOS 11+ (Big Sur or later) for native install<br>
            • Ubuntu 22.04+ or other modern 64‑bit Linux<br>
            • Windows 10 22H2+ / Windows 11 with WSL2<br><br>
        </span>
        <h3 style="color:#00bfff;">Hardware (recommended baseline):</h3>
        <span style="color:#00bfff;">
            • 16 GB RAM or more<br>
            • SSD with at least 12 GB free (256–512 GB recommended)<br>
            • 4–8 CPU cores<br><br>
        </span>
        <h3 style="color:#00bfff;">Developer Tools (optional but helpful):</h3>
        <span style="color:#00bfff;">
            • Git, Python, Node.js (if calling Ollama from code)<br>
            • Docker (if composing Ollama with other services)<br>
        </span>
    </td>
</tr>
<!-- Homebrew -->
<tr>
    <td style="padding:12px; width:25%; vertical-align:top;"><strong>2.1 Install Homebrew<br>(optional but handy)</strong></td>
    <td style="padding:12px;color:#00bfff; vertical-align:top;">
        <ol>
            <li>Open Terminal.</li>
            <li>Run:<br>
                <pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>
            </li>
            <li>Follow any post‑install instructions (e.g., add <code>eval "$(/opt/homebrew/bin/brew shellenv)"</code> to your shell profile).</li>
        </ol>
    </td>
</tr>

<!-- Ollama -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>2.2 Install Ollama</strong></td>
    <td style="padding:12px; color:#00bfff;vertical-align:top;">
        <p><strong>Option A — Official macOS App</strong></p>
        <ol>
            <li>Go to <code>https://ollama.ai</code> and download the macOS installer.</li>
            <li>Run the <code>.dmg</code> installer and follow the prompts. This will:
                <ul>
                    <li>Install the desktop app</li>
                    <li>Start the Ollama server in the background</li>
                    <li>Configure it to start on boot</li>
                </ul>
            </li>
        </ol>
        <p><strong>Option B — Homebrew</strong></p>
         <ol>
            <li><code>brew install ollama</code></li>
            <li><code>brew services start ollama</code></li>
            <li>API will be available at http://localhost:11434</li>
        </ol>
    </td>
</tr>
<!-- Verify -->
<tr>
    <td style="padding:12px; vertical-align:top;"><strong>2.3 Verify Server & Run a Model</strong></td>
    <td style="padding:12px; color:#00bfff;vertical-align:top;">
        <ol>
            <li>Open a browser and visit <code>http://localhost:11434/</code> — you should see “Ollama is running”.</li>
            <li>Pull and run a model, for example:<br>
                <pre><code>ollama run llama3.2</code></pre>
            </li>
        </ol>
    </td>
</tr>
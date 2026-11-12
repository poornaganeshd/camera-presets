import { createFileRoute } from "@tanstack/react-router";
import { Download } from "lucide-react";
import { useEffect, useState } from "react";

export const Route = createFileRoute("/")({ component: Home });

type Preset = {
  id: string;
  name: string;
  job: string;
  frames: number;
  lens_mm: number;
};

function Home() {
  const [presets, setPresets] = useState<Preset[]>([]);
  const [status, setStatus] = useState("Saving…");

  useEffect(() => {
    let cancelled = false;
    fetch("/pack/presets.json")
      .then((res) => res.json())
      .then((pack: { presets: Preset[] }) => {
        if (!cancelled) setPresets(pack.presets);
      })
      .catch(() => {
        if (!cancelled) setStatus("Couldn’t load the preset list.");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  async function saveZip() {
    setStatus("Saving…");
    try {
      const res = await fetch("/prop-room-cameras.zip");
      if (!res.ok) throw new Error(String(res.status));
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "prop-room-cameras.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.setTimeout(() => URL.revokeObjectURL(url), 1500);
      setStatus("Download started. Check your downloads folder.");
    } catch {
      setStatus("Popup blocked. Use the direct link under the button.");
      window.open("/prop-room-cameras.zip", "_blank", "noopener");
    }
  }

  return (
    <main className="stage">
      <p className="kicker">Camera presets</p>
      <h1>Prop Room Cameras</h1>
      <p className="lede">
        Thirteen moves for a flat character in a lit room. One zip to upload to Claude.
      </p>
      <button className="download" type="button" onClick={saveZip}>
        <Download aria-hidden="true" />
        Download zip
      </button>
      <p className="status">{status === "Saving…" ? "" : status}</p>
      <a className="direct" href="/prop-room-cameras.zip" target="_blank" rel="noopener">
        Open the zip file
      </a>
      <ol className="cards">
        {presets.map((preset) => (
          <li key={preset.id}>
            <span className="id">{preset.id}</span>
            <strong>{preset.name}</strong>
            <span className="meta">
              {preset.lens_mm}mm · {(preset.frames / 30).toFixed(1)}s
            </span>
            <p>{preset.job}</p>
          </li>
        ))}
      </ol>
    </main>
  );
}

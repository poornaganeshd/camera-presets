import { i as __toESM } from "../_runtime.mjs";
import { K as require_react, b as require_jsx_runtime } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as Download } from "../_libs/lucide-react.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/routes-Cv0Y_oVX.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function Home() {
	const [presets, setPresets] = (0, import_react.useState)([]);
	const [status, setStatus] = (0, import_react.useState)("Saving…");
	(0, import_react.useEffect)(() => {
		let cancelled = false;
		fetch("/pack/presets.json").then((res) => res.json()).then((pack) => {
			if (!cancelled) setPresets(pack.presets);
		}).catch(() => {
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
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
		className: "stage",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "kicker",
				children: "Camera presets"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", { children: "Prop Room Cameras" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "lede",
				children: "Thirteen moves for a flat character in a lit room. One zip to upload to Claude."
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
				className: "download",
				type: "button",
				onClick: saveZip,
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Download, { "aria-hidden": "true" }), "Download zip"]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "status",
				children: status === "Saving…" ? "" : status
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("a", {
				className: "direct",
				href: "/prop-room-cameras.zip",
				target: "_blank",
				rel: "noopener",
				children: "Open the zip file"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ol", {
				className: "cards",
				children: presets.map((preset) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", { children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "id",
						children: preset.id
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("strong", { children: preset.name }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
						className: "meta",
						children: [
							preset.lens_mm,
							"mm · ",
							(preset.frames / 30).toFixed(1),
							"s"
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { children: preset.job })
				] }, preset.id))
			})
		]
	});
}
//#endregion
export { Home as component };

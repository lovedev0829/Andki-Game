import{S as B,i as U,s as q,a as W,V as h,g as F,h as v,q as I,r as g,u as L,v as w,f as E,W as H,R as M,e as X,c as Y,b as j,D,N as d,t as z,d as G,k as J,X as K,U as O,Y as k,B as b,C as V,F as R,H as P}from"../chunks/Component.-XTVY6ph.mjs";import"../chunks/index.HrFqG6o2.mjs";const Q="modulepreload",Z=function(a,e){return new URL(a,e).href},y={},m=function(e,n,i){let r=Promise.resolve();if(n&&n.length>0){const f=document.getElementsByTagName("link");r=Promise.all(n.map(t=>{if(t=Z(t,i),t in y)return;y[t]=!0;const o=t.endsWith(".css"),l=o?'[rel="stylesheet"]':"";if(!!i)for(let u=f.length-1;u>=0;u--){const p=f[u];if(p.href===t&&(!o||p.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${t}"]${l}`))return;const s=document.createElement("link");if(s.rel=o?"stylesheet":Q,o||(s.as="script",s.crossOrigin=""),s.href=t,document.head.appendChild(s),o)return new Promise((u,p)=>{s.addEventListener("load",u),s.addEventListener("error",()=>p(new Error(`Unable to preload CSS for ${t}`)))})}))}return r.then(()=>e()).catch(f=>{const t=new Event("vite:preloadError",{cancelable:!0});if(t.payload=f,window.dispatchEvent(t),!t.defaultPrevented)throw f})},oe={};function $(a){let e,n,i;var r=a[1][0];function f(t,o){return{props:{data:t[3],form:t[2]}}}return r&&(e=k(r,f(a)),a[12](e)),{c(){e&&b(e.$$.fragment),n=h()},l(t){e&&V(e.$$.fragment,t),n=h()},m(t,o){e&&R(e,t,o),v(t,n,o),i=!0},p(t,o){if(o&2&&r!==(r=t[1][0])){if(e){I();const l=e;g(l.$$.fragment,1,0,()=>{P(l,1)}),L()}r?(e=k(r,f(t)),t[12](e),b(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(r){const l={};o&8&&(l.data=t[3]),o&4&&(l.form=t[2]),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&E(n),a[12](null),e&&P(e,t)}}}function x(a){let e,n,i;var r=a[1][0];function f(t,o){return{props:{data:t[3],$$slots:{default:[ee]},$$scope:{ctx:t}}}}return r&&(e=k(r,f(a)),a[11](e)),{c(){e&&b(e.$$.fragment),n=h()},l(t){e&&V(e.$$.fragment,t),n=h()},m(t,o){e&&R(e,t,o),v(t,n,o),i=!0},p(t,o){if(o&2&&r!==(r=t[1][0])){if(e){I();const l=e;g(l.$$.fragment,1,0,()=>{P(l,1)}),L()}r?(e=k(r,f(t)),t[11](e),b(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(r){const l={};o&8&&(l.data=t[3]),o&8215&&(l.$$scope={dirty:o,ctx:t}),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&E(n),a[11](null),e&&P(e,t)}}}function ee(a){let e,n,i;var r=a[1][1];function f(t,o){return{props:{data:t[4],form:t[2]}}}return r&&(e=k(r,f(a)),a[10](e)),{c(){e&&b(e.$$.fragment),n=h()},l(t){e&&V(e.$$.fragment,t),n=h()},m(t,o){e&&R(e,t,o),v(t,n,o),i=!0},p(t,o){if(o&2&&r!==(r=t[1][1])){if(e){I();const l=e;g(l.$$.fragment,1,0,()=>{P(l,1)}),L()}r?(e=k(r,f(t)),t[10](e),b(e.$$.fragment),w(e.$$.fragment,1),R(e,n.parentNode,n)):e=null}else if(r){const l={};o&16&&(l.data=t[4]),o&4&&(l.form=t[2]),e.$set(l)}},i(t){i||(e&&w(e.$$.fragment,t),i=!0)},o(t){e&&g(e.$$.fragment,t),i=!1},d(t){t&&E(n),a[10](null),e&&P(e,t)}}}function T(a){let e,n=a[6]&&A(a);return{c(){e=X("div"),n&&n.c(),this.h()},l(i){e=Y(i,"DIV",{id:!0,"aria-live":!0,"aria-atomic":!0,style:!0});var r=j(e);n&&n.l(r),r.forEach(E),this.h()},h(){D(e,"id","svelte-announcer"),D(e,"aria-live","assertive"),D(e,"aria-atomic","true"),d(e,"position","absolute"),d(e,"left","0"),d(e,"top","0"),d(e,"clip","rect(0 0 0 0)"),d(e,"clip-path","inset(50%)"),d(e,"overflow","hidden"),d(e,"white-space","nowrap"),d(e,"width","1px"),d(e,"height","1px")},m(i,r){v(i,e,r),n&&n.m(e,null)},p(i,r){i[6]?n?n.p(i,r):(n=A(i),n.c(),n.m(e,null)):n&&(n.d(1),n=null)},d(i){i&&E(e),n&&n.d()}}}function A(a){let e;return{c(){e=z(a[7])},l(n){e=G(n,a[7])},m(n,i){v(n,e,i)},p(n,i){i&128&&J(e,n[7])},d(n){n&&E(e)}}}function te(a){let e,n,i,r,f;const t=[x,$],o=[];function l(s,u){return s[1][1]?0:1}e=l(a),n=o[e]=t[e](a);let _=a[5]&&T(a);return{c(){n.c(),i=W(),_&&_.c(),r=h()},l(s){n.l(s),i=F(s),_&&_.l(s),r=h()},m(s,u){o[e].m(s,u),v(s,i,u),_&&_.m(s,u),v(s,r,u),f=!0},p(s,[u]){let p=e;e=l(s),e===p?o[e].p(s,u):(I(),g(o[p],1,1,()=>{o[p]=null}),L(),n=o[e],n?n.p(s,u):(n=o[e]=t[e](s),n.c()),w(n,1),n.m(i.parentNode,i)),s[5]?_?_.p(s,u):(_=T(s),_.c(),_.m(r.parentNode,r)):_&&(_.d(1),_=null)},i(s){f||(w(n),f=!0)},o(s){g(n),f=!1},d(s){s&&(E(i),E(r)),o[e].d(s),_&&_.d(s)}}}function ne(a,e,n){let{stores:i}=e,{page:r}=e,{constructors:f}=e,{components:t=[]}=e,{form:o}=e,{data_0:l=null}=e,{data_1:_=null}=e;H(i.page.notify);let s=!1,u=!1,p=null;M(()=>{const c=i.page.subscribe(()=>{s&&(n(6,u=!0),K().then(()=>{n(7,p=document.title||"untitled page")}))});return n(5,s=!0),c});function N(c){O[c?"unshift":"push"](()=>{t[1]=c,n(0,t)})}function S(c){O[c?"unshift":"push"](()=>{t[0]=c,n(0,t)})}function C(c){O[c?"unshift":"push"](()=>{t[0]=c,n(0,t)})}return a.$$set=c=>{"stores"in c&&n(8,i=c.stores),"page"in c&&n(9,r=c.page),"constructors"in c&&n(1,f=c.constructors),"components"in c&&n(0,t=c.components),"form"in c&&n(2,o=c.form),"data_0"in c&&n(3,l=c.data_0),"data_1"in c&&n(4,_=c.data_1)},a.$$.update=()=>{a.$$.dirty&768&&i.page.set(r)},[t,f,o,l,_,s,u,p,i,r,N,S,C]}class se extends B{constructor(e){super(),U(this,e,ne,te,q,{stores:8,page:9,constructors:1,components:0,form:2,data_0:3,data_1:4})}}const ae=[()=>m(()=>import("../nodes/0.b65RHLlA.mjs"),__vite__mapDeps([0,1,2,3,4,5,6,7]),import.meta.url),()=>m(()=>import("../nodes/1.dC1TvN08.mjs"),__vite__mapDeps([8,4,5,9,10,11]),import.meta.url),()=>m(()=>import("../nodes/2.8Jdk5FYl.mjs"),__vite__mapDeps([12,3,4,5,9,10,11,13,14,15,16,17,18,19,20]),import.meta.url),()=>m(()=>import("../nodes/3.35TeEeym.mjs"),__vite__mapDeps([21,3,17,11,4,22,23,24,5,6,25,26,27,28,18,29,30,31,32,13,14,15,16,33,34,35,36,37,38,39,40,41,42]),import.meta.url),()=>m(()=>import("../nodes/4.Z9YPCgWH.mjs"),__vite__mapDeps([43,3,4,5,17,44,26,31,32,13,14,19,45]),import.meta.url),()=>m(()=>import("../nodes/5.zkFAmymI.mjs"),__vite__mapDeps([46,3,1,2,11,4,47,23,24,5,6,25,17,26,27,28,22,18,29,13,14,15,16,48,49,30,50,51,36,52,53,54,55,31,32,56,35,37,33,34,38,39,57,19,58]),import.meta.url),()=>m(()=>import("../nodes/6.Tg8suTAk.mjs"),__vite__mapDeps([59,4,5,17,3,19,51,36,26,11,52,1,2,24,18,44,60,61]),import.meta.url),()=>m(()=>import("../nodes/7.uIj4_ZXq.mjs"),__vite__mapDeps([62,4,5,63,18,17,3,13,14,11,2,54,25,26,27,55,64,49,23,24,6,28,65,66,36,67,47,31,32,15,16,68]),import.meta.url),()=>m(()=>import("../nodes/8.buyxxwkK.mjs"),__vite__mapDeps([69,3,4,5,17,53,18,30,2,54,25,26,27,55,23,24,6,11,28,36,31,32,15,16,22,29,47,56,51,52,70,57,13,14,38,39,44,65,66,71]),import.meta.url),()=>m(()=>import("../nodes/9.DOuvq-qf.mjs"),__vite__mapDeps([72,3,17,11,4,47,23,24,5,6,25,26,27,28,22,18,29,15,16,70,57,36,13,14,38,39,44,54,2,55,65,66,71,60,51,52,31,32,53,30,56,64,49,67,73]),import.meta.url),()=>m(()=>import("../nodes/10.u1FzTYYW.mjs"),__vite__mapDeps([74,4,5,3,70,57,36,26,11,13,14,17,25,27,38,39,18,44,54,2,55,65,66,71]),import.meta.url),()=>m(()=>import("../nodes/11.LNI6CmX2.mjs"),__vite__mapDeps([75,26,4,5,18,60,48,49,30,11,50,17,3,1,2,6,54,25,27,55,38,39,23,24,28,35,36,37,44,64,65,66,67,63,13,14,47,31,32,15,16,68,40,41,76]),import.meta.url)],le=[],ce={"/card-info/[cardId]":[2],"/change-notetype/[...notetypeIds]":[3],"/congrats":[4],"/deck-options/[deckId]":[5],"/graphs":[6],"/image-occlusion/[...imagePathOrNoteId]":[7],"/import-anki-package/[...path]":[8],"/import-csv/[...path]":[9],"/import-page/[...path]":[10],"/tmp":[11]},fe={handleError:({error:a})=>{console.error(a)},reroute:()=>{}};export{ce as dictionary,fe as hooks,oe as matchers,ae as nodes,se as root,le as server_loads};
function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["../nodes/0.b65RHLlA.mjs","../chunks/utils.ARvOduQt.mjs","../chunks/_commonjsHelpers.1J56E-h6.mjs","../chunks/backend.pzQSPd-R.mjs","../chunks/Component.-XTVY6ph.mjs","../chunks/index.HrFqG6o2.mjs","../chunks/context-keys.O6kwXuuk.mjs","../assets/0.IueIF_dt.css","../nodes/1.dC1TvN08.mjs","../chunks/stores.eGE0cfsR.mjs","../chunks/entry.rhBufsQE.mjs","../chunks/index.grcEGtIt.mjs","../nodes/2.8Jdk5FYl.mjs","../chunks/Container.T7flwP-u.mjs","../assets/Container.eXhp69HK.css","../chunks/Row.9I620FT8.mjs","../assets/Row.b7XJyprP.css","../chunks/ftl.cKofWsqB.mjs","../chunks/each.mrBeHWFK.mjs","../chunks/time.KwyxY_gf.mjs","../assets/2.bbjb279y.css","../nodes/3.35TeEeym.mjs","../chunks/Select.R1roNBxL.mjs","../chunks/Badge.EYzNN-L8.mjs","../chunks/isObject.u1V2KUQz.mjs","../chunks/Shortcut.F_v_rQsz.mjs","../chunks/runtime-require.2UnWAaTy.mjs","../assets/Shortcut.OA7NpPBO.css","../assets/Badge.v6qaTRgw.css","../assets/Select.518aewif.css","../chunks/helpers.Gx5FBjbA.mjs","../chunks/Col.0MgQrJqK.mjs","../assets/Col.qcAwB6Pe.css","../chunks/StickyContainer.GIYfErNx.mjs","../assets/StickyContainer.DxeQbxYa.css","../chunks/index.TzTdlOlB.mjs","../chunks/theme.0LplNH_j.mjs","../assets/index.3xYXG4Hb.css","../chunks/LabelButton.cYtwXhrB.mjs","../assets/LabelButton.veMCivba.css","../chunks/ButtonGroup.d7QDvkED.mjs","../assets/ButtonGroup.uVxANZ_b.css","../assets/3.qxaop3gC.css","../nodes/4.Z9YPCgWH.mjs","../chunks/bridgecommand._LcBipD7.mjs","../assets/4.m6aFTiDT.css","../nodes/5.zkFAmymI.mjs","../chunks/cloneDeep.8E2eT3Ku.mjs","../chunks/functional.jxrS5nAj.mjs","../chunks/cross-browser.a5UeKJFq.mjs","../assets/functional.6WG_Obrt.css","../chunks/TitledContainer.hh0V9Qqi.mjs","../assets/TitledContainer.Pwt2MqSt.css","../chunks/EnumSelectorRow._-wvplcD.mjs","../chunks/IconButton.NEW1XP5_.mjs","../assets/IconButton.Q3-fLyR3.css","../assets/EnumSelectorRow.QQEOXXCA.css","../chunks/progress.K1KExmpd.mjs","../assets/5.OYlHvTyA.css","../nodes/6.Tg8suTAk.mjs","../chunks/await_block.5NvcH_hP.mjs","../assets/6.T9GipAsA.css","../nodes/7.uIj4_ZXq.mjs","../chunks/ImageOcclusionPage.YZT9hres.mjs","../chunks/TagEditor.WwIHJlIr.mjs","../chunks/WithTooltip.ERYnIwCM.mjs","../assets/WithTooltip.Q8RzqOIi.css","../assets/TagEditor.7UpmKeav.css","../assets/ImageOcclusionPage.A9p62vyw.css","../nodes/8.buyxxwkK.mjs","../chunks/ImportPage.Ru8SBaMG.mjs","../assets/ImportPage.6VNQDQcV.css","../nodes/9.DOuvq-qf.mjs","../assets/9.fajENBT1.css","../nodes/10.u1FzTYYW.mjs","../nodes/11.LNI6CmX2.mjs","../assets/11.dpLQQhZc.css"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}

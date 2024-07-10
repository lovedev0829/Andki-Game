var De=Object.defineProperty;var Te=(o,e,r)=>e in o?De(o,e,{enumerable:!0,configurable:!0,writable:!0,value:r}):o[e]=r;var V=(o,e,r)=>(Te(o,typeof e!="symbol"?e+"":e,r),r);import{w as ve,x as Fe,p as Ve}from"../chunks/backend.WLkVIN8Y.mjs";import{al as Ee,aP as Oe,aQ as Be,aR as ze,aS as Le,aT as je,aU as Pe,aV as Ae,aW as Me,aX as Re,aY as qe}from"../chunks/ftl.kZuA-e76.mjs";import{r as re}from"../chunks/index.JQ1vVYlZ.mjs";import{i as se,S as Z}from"../chunks/Select.SmZfnapu.mjs";import{S as j,i as P,s as A,z as N,A as I,B as k,d as m,C as z,a as _,n as E,v as g,w as h,x as b,m as c,k as p,y as v,e as G,J as D,K as T,t as O,c as B,b as H,M as w,Z as R,j as U,l as X,a3 as we,N as F,V as He,X as We,Y as Ue,D as Xe,a9 as Ye,aa as Ge,P as le,u as Je,r as Ke,q as ye,a1 as Qe,a2 as Ze}from"../chunks/Component.XCUzfIB4.mjs";import"../chunks/index.HrFqG6o2.mjs";import{a as xe}from"../chunks/helpers.Gx5FBjbA.mjs";import{C as x}from"../chunks/Container.Od8kXvHE.mjs";import{R as q}from"../chunks/Row.3S4P0t9A.mjs";import{S as et}from"../chunks/StickyContainer.bIa-NGCP.mjs";import{T as Ne}from"../chunks/TitledContainer.EN_ruWEJ.mjs";import{e as J}from"../chunks/each.W4AIRH3O.mjs";import{C as K}from"../chunks/Col.tApfF0fT.mjs";import{B as tt}from"../chunks/ButtonToolbar.dmCdVnWM.mjs";import{b as nt,S as rt,I as ee,c as st,d as lt,p as at,o as ae,m as ot}from"../chunks/Shortcut.P7PDYf7j.mjs";import{B as it}from"../chunks/ButtonGroup.xBvkeKV2.mjs";import{L as ft}from"../chunks/LabelButton.naCfMegJ.mjs";import{s as oe}from"../chunks/index.T68qPqOw.mjs";import{B as ut}from"../chunks/Badge.-WspKHvV.mjs";function ie(o){return o.map(e=>e!=null?e:-1)}function fe(o){return o.map(e=>e===-1?null:e)}class ue{constructor(e){V(this,"fields");V(this,"templates");V(this,"oldNotetypeName");V(this,"isCloze");V(this,"info");var t,n,s,l,a,i;this.info=e;const r=(n=(t=e.input)==null?void 0:t.newTemplates)!=null?n:[];this.isCloze=(l=(s=e.input)==null?void 0:s.isCloze)!=null?l:!1,r.length>0&&(this.templates=fe(r)),this.fields=fe((i=(a=e.input)==null?void 0:a.newFields)!=null?i:[]),this.oldNotetypeName=e.oldNotetypeName}mapForContext(e){var r;return e==1?(r=this.templates)!=null?r:[]:this.fields}getOldIndex(e,r){const n=this.mapForContext(e)[r];return n!=null?n:this.getOldNamesIncludingNothing(e).length-1}getOldNamesIncludingNothing(e){return[...this.getOldNames(e),Ee()]}getOldNames(e){return e==1?this.info.oldTemplateNames:this.info.oldFieldNames}getOldNotetypeName(){return this.info.oldNotetypeName}getNewName(e,r){return(e==1?this.info.newTemplateNames:this.info.newFieldNames)[r]}unusedItems(e){const r=new Set(this.mapForContext(e).filter(l=>l!==null)),t=this.getOldNames(e);return[...Array(t.length).keys()].filter(l=>!r.has(l)).map(l=>t[l])}unchanged(){var e,r;return this.input().newNotetypeId===this.input().oldNotetypeId&&se(this.fields,[...Array(this.fields.length).keys()])&&se(this.templates,[...Array((r=(e=this.templates)==null?void 0:e.length)!=null?r:0).keys()])}input(){return this.info.input}intoInput(){const e=this.info.input;return e.newFields=ie(this.fields),this.templates&&(e.newTemplates=ie(this.templates)),e}}var L=(o=>(o[o.Field=0]="Field",o[o.Template=1]="Template",o))(L||{});class ct{constructor(e,r){V(this,"info");V(this,"notetypes");V(this,"info_");V(this,"infoSetter");V(this,"notetypeNames");V(this,"notetypesSetter");this.info_=new ue(r),this.info=re(this.info_,t=>{this.infoSetter=t}),this.notetypeNames=e,this.notetypes=re(this.buildNotetypeList(),t=>{this.notetypesSetter=t})}async setTargetNotetypeIndex(e){this.info_.input().newNotetypeId=this.notetypeNames.entries[e].id,this.notetypesSetter(this.buildNotetypeList());const{oldNotetypeId:r,newNotetypeId:t}=this.info_.input(),n=await ve({oldNotetypeId:r,newNotetypeId:t});this.info_=new ue(n),this.info_.unusedItems(0),this.infoSetter(this.info_)}setOldIndex(e,r,t){const n=this.info_.mapForContext(e),s=this.info_.getOldNames(e),l=t<s.length?t:null;if(!(e==0)&&l!==null)for(let i=0;i<n.length;i++)n[i]===l&&(n[i]=null);n[r]=l,this.infoSetter(this.info_)}dataForSaving(){return this.info_.intoInput()}async save(){if(this.info_.unchanged()){alert("No changes to save");return}await Fe(this.dataForSaving())}buildNotetypeList(){const e=this.info_.input().newNotetypeId;return this.notetypeNames.entries.map((r,t)=>({idx:t,name:r.name,current:r.id===e}))}}const $t=async({params:o})=>{const[e,r]=o.notetypeIds.split("/"),t=BigInt(e),n=r?BigInt(r):t,s=Ve({}),l=ve({oldNotetypeId:t,newNotetypeId:n}),[a,i]=await Promise.all([s,l]);return{state:new ct(a,i)}},Tn=Object.freeze(Object.defineProperty({__proto__:null,load:$t},Symbol.toStringTag,{value:"Module"}));function mt(o){let e;return{c(){e=N("div"),this.h()},l(r){e=I(r,"DIV",{class:!0}),k(e).forEach(m),this.h()},h(){z(e,"class","svelte-1xardfc")},m(r,t){_(r,e,t)},p:E,i:E,o:E,d(r){r&&m(e)}}}class pt extends j{constructor(e){super(),P(this,e,null,mt,A,{})}}function dt(o){let e,r;return e=new Z({props:{value:o[2],label:o[4],list:o[3].getOldNamesIncludingNothing(o[0])}}),e.$on("change",o[6]),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&4&&(s.value=t[2]),n&16&&(s.label=t[4]),n&9&&(s.list=t[3].getOldNamesIncludingNothing(t[0])),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function _t(o){let e=o[3].getNewName(o[0],o[1])+"",r;return{c(){r=O(e)},l(t){r=B(t,e)},m(t,n){_(t,r,n)},p(t,n){n&11&&e!==(e=t[3].getNewName(t[0],t[1])+"")&&H(r,e)},d(t){t&&m(r)}}}function gt(o){let e,r,t,n;return e=new K({props:{$$slots:{default:[dt]},$$scope:{ctx:o}}}),t=new K({props:{$$slots:{default:[_t]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment),r=D(),g(t.$$.fragment)},l(s){h(e.$$.fragment,s),r=T(s),h(t.$$.fragment,s)},m(s,l){b(e,s,l),_(s,r,l),b(t,s,l),n=!0},p(s,l){const a={};l&285&&(a.$$scope={dirty:l,ctx:s}),e.$set(a);const i={};l&267&&(i.$$scope={dirty:l,ctx:s}),t.$set(i)},i(s){n||(c(e.$$.fragment,s),c(t.$$.fragment,s),n=!0)},o(s){p(e.$$.fragment,s),p(t.$$.fragment,s),n=!1},d(s){s&&m(r),v(e,s),v(t,s)}}}function ht(o){let e,r;return e=new q({props:{$$slots:{default:[gt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,[n]){const s={};n&287&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function bt(o,e,r){let t,n,s,{state:l}=e,{ctx:a}=e,{newIndex:i}=e;const u=l.info;G(o,u,$=>r(3,s=$));function f($){r(2,t=$.detail.value),l.setOldIndex(a,i,t)}return o.$$set=$=>{"state"in $&&r(7,l=$.state),"ctx"in $&&r(0,a=$.ctx),"newIndex"in $&&r(1,i=$.newIndex)},o.$$.update=()=>{o.$$.dirty&11&&r(2,t=s.getOldIndex(a,i)),o.$$.dirty&13&&r(4,n=s.getOldNamesIncludingNothing(a)[t])},[a,i,t,s,n,u,f,l]}class vt extends j{constructor(e){super(),P(this,e,bt,ht,A,{state:7,ctx:0,newIndex:1})}}function ce(o,e,r){const t=o.slice();return t[4]=e[r],t[6]=r,t}function $e(o){let e,r;return e=new vt({props:{state:o[0],ctx:o[1],newIndex:o[6]}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&1&&(s.state=t[0]),n&2&&(s.ctx=t[1]),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function wt(o){let e,r,t=J(o[2].mapForContext(o[1])),n=[];for(let l=0;l<t.length;l+=1)n[l]=$e(ce(o,t,l));const s=l=>p(n[l],1,1,()=>{n[l]=null});return{c(){for(let l=0;l<n.length;l+=1)n[l].c();e=R()},l(l){for(let a=0;a<n.length;a+=1)n[a].l(l);e=R()},m(l,a){for(let i=0;i<n.length;i+=1)n[i]&&n[i].m(l,a);_(l,e,a),r=!0},p(l,a){if(a&7){t=J(l[2].mapForContext(l[1]));let i;for(i=0;i<t.length;i+=1){const u=ce(l,t,i);n[i]?(n[i].p(u,a),c(n[i],1)):(n[i]=$e(u),n[i].c(),c(n[i],1),n[i].m(e.parentNode,e))}for(U(),i=t.length;i<n.length;i+=1)s(i);X()}},i(l){if(!r){for(let a=0;a<t.length;a+=1)c(n[a]);r=!0}},o(l){n=n.filter(Boolean);for(let a=0;a<n.length;a+=1)p(n[a]);r=!1},d(l){l&&m(e),we(n,l)}}}function yt(o){let e,r,t,n,s,l;return e=new pt({}),n=new x({props:{$$slots:{default:[wt]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),t=D(),s=N("div"),g(n.$$.fragment),this.h()},l(a){r=I(a,"DIV",{style:!0});var i=k(r);h(e.$$.fragment,i),t=T(a),s=I(a,"DIV",{style:!0});var u=k(s);h(n.$$.fragment,u),this.h()},h(){w(r,"display","contents"),w(r,"--height","0.5rem"),w(s,"display","contents"),w(s,"--gutter-inline","0.5rem"),w(s,"--gutter-block","0.15rem")},m(a,i){_(a,r,i),b(e,r,null),_(a,t,i),_(a,s,i),b(n,s,null),l=!0},p(a,[i]){const u={};i&135&&(u.$$scope={dirty:i,ctx:a}),n.$set(u)},i(a){l||(c(e.$$.fragment,a),c(n.$$.fragment,a),l=!0)},o(a){p(e.$$.fragment,a),p(n.$$.fragment,a),l=!1},d(a){a&&m(t),a&&e&&m(r),v(e,a),a&&n&&m(s),v(n,a)}}}function Nt(o,e,r){let t,{state:n}=e,{ctx:s}=e;const l=n.info;return G(o,l,a=>r(2,t=a)),o.$$set=a=>{"state"in a&&r(0,n=a.state),"ctx"in a&&r(1,s=a.ctx)},[n,s,t,l]}class Ie extends j{constructor(e){super(),P(this,e,Nt,yt,A,{state:0,ctx:1})}}function It(o){let e,r=Oe()+"",t;return{c(){e=N("div"),t=O(r),this.h()},l(n){e=I(n,"DIV",{class:!0});var s=k(e);t=B(s,r),s.forEach(m),this.h()},h(){z(e,"class","save svelte-1polrdz")},m(n,s){_(n,e,s),F(e,t)},p:E,d(n){n&&m(e)}}}function kt(o){let e,r,t,n,s;return e=new ft({props:{primary:!0,tooltip:nt(me),$$slots:{default:[It]},$$scope:{ctx:o}}}),e.$on("click",o[0]),n=new rt({props:{keyCombination:me}}),n.$on("action",o[0]),{c(){r=N("div"),g(e.$$.fragment),t=D(),g(n.$$.fragment),this.h()},l(l){r=I(l,"DIV",{style:!0});var a=k(r);h(e.$$.fragment,a),t=T(l),h(n.$$.fragment,l),this.h()},h(){w(r,"display","contents"),w(r,"--border-left-radius","5px"),w(r,"--border-right-radius","5px")},m(l,a){_(l,r,a),b(e,r,null),_(l,t,a),b(n,l,a),s=!0},p(l,a){const i={};a&4&&(i.$$scope={dirty:a,ctx:l}),e.$set(i)},i(l){s||(c(e.$$.fragment,l),c(n.$$.fragment,l),s=!0)},o(l){p(e.$$.fragment,l),p(n.$$.fragment,l),s=!1},d(l){l&&m(t),l&&e&&m(r),v(e,l),v(n,l)}}}function St(o){let e,r;return e=new it({props:{$$slots:{default:[kt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,[n]){const s={};n&4&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}const me="Control+Enter";function Ct(o,e,r){let{state:t}=e;function n(){document.activeElement instanceof HTMLElement&&document.activeElement.blur(),t.save()}return o.$$set=s=>{"state"in s&&r(1,t=s.state)},[n,t]}class Dt extends j{constructor(e){super(),P(this,e,Ct,St,A,{state:1})}}function Tt(o){let e,r;return e=new ee({props:{icon:st}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Ft(o){let e,r;return e=new ee({props:{icon:lt}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Vt(o){let e,r,t,n,s,l,a,i,u,f,$,d;r=new Z({props:{label:o[4].oldNotetypeName,value:1,list:[1],disabled:!0}});const S=[Ft,Tt],Q=[];function Se(y,C){return window.getComputedStyle(document.body).direction=="rtl"?0:1}s=Se(),l=Q[s]=S[s](o);function Ce(y){o[8](y)}let te={list:o[2],label:o[3]};return o[1]!==void 0&&(te.value=o[1]),i=new Z({props:te}),He.push(()=>We(i,"value",Ce)),$=new Dt({props:{state:o[0]}}),{c(){e=N("div"),g(r.$$.fragment),t=D(),n=N("div"),l.c(),a=D(),g(i.$$.fragment),f=D(),g($.$$.fragment),this.h()},l(y){e=I(y,"DIV",{class:!0});var C=k(e);h(r.$$.fragment,C),t=T(C),n=I(C,"DIV",{class:!0});var W=k(n);l.l(W),W.forEach(m),a=T(C),h(i.$$.fragment,C),C.forEach(m),f=T(y),h($.$$.fragment,y),this.h()},h(){z(n,"class","arrow-container svelte-ng49hq"),z(e,"class","d-flex flex-row w-100")},m(y,C){_(y,e,C),b(r,e,null),F(e,t),F(e,n),Q[s].m(n,null),F(e,a),b(i,e,null),_(y,f,C),b($,y,C),d=!0},p(y,C){const W={};C&16&&(W.label=y[4].oldNotetypeName),r.$set(W);const Y={};C&4&&(Y.list=y[2]),C&8&&(Y.label=y[3]),!u&&C&2&&(u=!0,Y.value=y[1],Ue(()=>u=!1)),i.$set(Y);const ne={};C&1&&(ne.state=y[0]),$.$set(ne)},i(y){d||(c(r.$$.fragment,y),c(l),c(i.$$.fragment,y),c($.$$.fragment,y),d=!0)},o(y){p(r.$$.fragment,y),p(l),p(i.$$.fragment,y),p($.$$.fragment,y),d=!1},d(y){y&&(m(e),m(f)),v(r),Q[s].d(),v(i),v($,y)}}}function Et(o){let e,r;return e=new tt({props:{class:"justify-content-between",wrap:!1,$$slots:{default:[Vt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,[n]){const s={};n&543&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Ot(o,e,r){let t,n,s,l,{state:a}=e;const i=a.notetypes;G(o,i,d=>r(7,s=d));const u=a.info;G(o,u,d=>r(4,l=d));let f=s.findIndex(d=>d.current);function $(d){f=d,r(1,f)}return o.$$set=d=>{"state"in d&&r(0,a=d.state)},o.$$.update=()=>{o.$$.dirty&128&&r(2,t=Array.from(s,d=>d.name)),o.$$.dirty&6&&r(3,n=t[f]),o.$$.dirty&3&&a.setTargetNotetypeIndex(f)},[a,f,t,n,l,i,u,s,$]}class Bt extends j{constructor(e){super(),P(this,e,Ot,Et,A,{state:0})}}function pe(o,e,r){const t=o.slice();return t[8]=e[r],t}function de(o){let e,r,t,n,s,l,a,i;return r=new ut({props:{iconSize:80,$$slots:{default:[zt]},$$scope:{ctx:o}}}),{c(){e=N("div"),g(r.$$.fragment),t=D(),n=O(o[4]),this.h()},l(u){e=I(u,"DIV",{class:!0,role:!0,tabindex:!0,"aria-expanded":!0});var f=k(e);h(r.$$.fragment,f),t=T(f),n=B(f,o[4]),f.forEach(m),this.h()},h(){z(e,"class","clickable svelte-18ivrjn"),z(e,"role","button"),z(e,"tabindex","0"),z(e,"aria-expanded",s=!o[1])},m(u,f){_(u,e,f),b(r,e,null),F(e,t),F(e,n),l=!0,a||(i=[le(e,"click",o[6]),le(e,"keydown",function(){Je(ae(o[7]))&&ae(o[7]).apply(this,arguments)})],a=!0)},p(u,f){o=u;const $={};f&2056&&($.$$scope={dirty:f,ctx:o}),r.$set($),(!l||f&16)&&H(n,o[4]),(!l||f&2&&s!==(s=!o[1]))&&z(e,"aria-expanded",s)},i(u){l||(c(r.$$.fragment,u),l=!0)},o(u){p(r.$$.fragment,u),l=!1},d(u){u&&m(e),v(r),a=!1,Ke(i)}}}function zt(o){let e,r;return e=new ee({props:{icon:o[3]}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&8&&(s.icon=t[3]),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Lt(o){let e,r=J(o[0]),t=[];for(let n=0;n<r.length;n+=1)t[n]=_e(pe(o,r,n));return{c(){e=N("ul");for(let n=0;n<t.length;n+=1)t[n].c()},l(n){e=I(n,"UL",{});var s=k(e);for(let l=0;l<t.length;l+=1)t[l].l(s);s.forEach(m)},m(n,s){_(n,e,s);for(let l=0;l<t.length;l+=1)t[l]&&t[l].m(e,null)},p(n,s){if(s&1){r=J(n[0]);let l;for(l=0;l<r.length;l+=1){const a=pe(n,r,l);t[l]?t[l].p(a,s):(t[l]=_e(a),t[l].c(),t[l].m(e,null))}for(;l<t.length;l+=1)t[l].d(1);t.length=r.length}},d(n){n&&m(e),we(t,n)}}}function jt(o){let e,r=o[0].slice(0,M).join(", ")+"",t,n,s=o[0].length>M&&ge(o);return{c(){e=N("div"),t=O(r),n=D(),s&&s.c()},l(l){e=I(l,"DIV",{});var a=k(e);t=B(a,r),n=T(a),s&&s.l(a),a.forEach(m)},m(l,a){_(l,e,a),F(e,t),F(e,n),s&&s.m(e,null)},p(l,a){a&1&&r!==(r=l[0].slice(0,M).join(", ")+"")&&H(t,r),l[0].length>M?s?s.p(l,a):(s=ge(l),s.c(),s.m(e,null)):s&&(s.d(1),s=null)},d(l){l&&m(e),s&&s.d()}}}function _e(o){let e,r=o[8]+"",t;return{c(){e=N("li"),t=O(r)},l(n){e=I(n,"LI",{});var s=k(e);t=B(s,r),s.forEach(m)},m(n,s){_(n,e,s),F(e,t)},p(n,s){s&1&&r!==(r=n[8]+"")&&H(t,r)},d(n){n&&m(e)}}}function ge(o){let e,r=o[0].length-M+"",t,n;return{c(){e=O("... (+"),t=O(r),n=O(")")},l(s){e=B(s,"... (+"),t=B(s,r),n=B(s,")")},m(s,l){_(s,e,l),_(s,t,l),_(s,n,l)},p(s,l){l&1&&r!==(r=s[0].length-M+"")&&H(t,r)},d(s){s&&(m(e),m(t),m(n))}}}function Pt(o){let e,r,t,n,s,l,a,i=o[0].length>M&&de(o);function u(d,S){return d[1]?jt:Lt}let f=u(o),$=f(o);return{c(){e=N("div"),i&&i.c(),r=D(),t=O(o[2]),n=D(),$.c(),this.h()},l(d){e=I(d,"DIV",{class:!0});var S=k(e);i&&i.l(S),r=T(S),t=B(S,o[2]),n=T(S),$.l(S),S.forEach(m),this.h()},h(){z(e,"class","alert alert-warning")},m(d,S){_(d,e,S),i&&i.m(e,null),F(e,r),F(e,t),F(e,n),$.m(e,null),a=!0},p(d,[S]){d[0].length>M?i?(i.p(d,S),S&1&&c(i,1)):(i=de(d),i.c(),c(i,1),i.m(e,r)):i&&(U(),p(i,1,1,()=>{i=null}),X()),(!a||S&4)&&H(t,d[2]),f===(f=u(d))&&$?$.p(d,S):($.d(1),$=f(d),$&&($.c(),$.m(e,null)))},i(d){a||(c(i),d&&Xe(()=>{a&&(l&&l.end(1),s=Ye(e,oe,{}),s.start())}),a=!0)},o(d){p(i),s&&s.invalidate(),d&&(l=Ge(e,oe,{})),a=!1},d(d){d&&m(e),i&&i.d(),$.d(),d&&l&&l.end()}}}const M=3;function At(o,e,r){let t,n,{unused:s}=e,{ctx:l}=e,a,i=!0;const u=()=>r(1,i=!i),f=()=>r(1,i=!i);return o.$$set=$=>{"unused"in $&&r(0,s=$.unused),"ctx"in $&&r(5,l=$.ctx)},o.$$.update=()=>{o.$$.dirty&32&&r(2,a=l===L.Field?Be():ze()),o.$$.dirty&2&&r(4,t=i?Le():je()),o.$$.dirty&2&&r(3,n=i?at:ot)},[s,i,a,n,t,l,u,f]}class Mt extends j{constructor(e){super(),P(this,e,At,Pt,A,{unused:0,ctx:5})}}function he(o){let e,r;return e=new Mt({props:{unused:o[2],ctx:o[0]}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&4&&(s.unused=t[2]),n&1&&(s.ctx=t[0]),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function be(o){let e,r,t;return e=new x({props:{$$slots:{default:[Wt]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),this.h()},l(n){r=I(n,"DIV",{style:!0});var s=k(r);h(e.$$.fragment,s),this.h()},h(){w(r,"display","contents"),w(r,"--gutter-inline","0.5rem"),w(r,"--gutter-block","0.2rem")},m(n,s){_(n,r,s),b(e,r,null),t=!0},i(n){t||(c(e.$$.fragment,n),t=!0)},o(n){p(e.$$.fragment,n),t=!1},d(n){n&&e&&m(r),v(e,n)}}}function Rt(o){let e,r=Pe()+"",t;return{c(){e=N("b"),t=O(r)},l(n){e=I(n,"B",{});var s=k(e);t=B(s,r),s.forEach(m)},m(n,s){_(n,e,s),F(e,t)},p:E,d(n){n&&m(e)}}}function qt(o){let e,r=Ae()+"",t;return{c(){e=N("b"),t=O(r)},l(n){e=I(n,"B",{});var s=k(e);t=B(s,r),s.forEach(m)},m(n,s){_(n,e,s),F(e,t)},p:E,d(n){n&&m(e)}}}function Ht(o){let e,r,t,n,s,l;return e=new K({props:{$$slots:{default:[Rt]},$$scope:{ctx:o}}}),n=new K({props:{$$slots:{default:[qt]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),t=D(),s=N("div"),g(n.$$.fragment),this.h()},l(a){r=I(a,"DIV",{style:!0});var i=k(r);h(e.$$.fragment,i),t=T(a),s=I(a,"DIV",{style:!0});var u=k(s);h(n.$$.fragment,u),this.h()},h(){w(r,"display","contents"),w(r,"--col-size",1),w(s,"display","contents"),w(s,"--col-size",1)},m(a,i){_(a,r,i),b(e,r,null),_(a,t,i),_(a,s,i),b(n,s,null),l=!0},p(a,i){const u={};i&32&&(u.$$scope={dirty:i,ctx:a}),e.$set(u);const f={};i&32&&(f.$$scope={dirty:i,ctx:a}),n.$set(f)},i(a){l||(c(e.$$.fragment,a),c(n.$$.fragment,a),l=!0)},o(a){p(e.$$.fragment,a),p(n.$$.fragment,a),l=!1},d(a){a&&m(t),a&&e&&m(r),v(e,a),a&&n&&m(s),v(n,a)}}}function Wt(o){let e,r,t;return e=new q({props:{$$slots:{default:[Ht]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),this.h()},l(n){r=I(n,"DIV",{style:!0});var s=k(r);h(e.$$.fragment,s),this.h()},h(){w(r,"display","contents"),w(r,"--cols",2)},m(n,s){_(n,r,s),b(e,r,null),t=!0},p(n,s){const l={};s&32&&(l.$$scope={dirty:s,ctx:n}),e.$set(l)},i(n){t||(c(e.$$.fragment,n),t=!0)},o(n){p(e.$$.fragment,n),t=!1},d(n){n&&e&&m(r),v(e,n)}}}function Ut(o){let e,r,t,n=o[2].length>0&&he(o),s=(o[1].templates||o[0]===L.Field)&&be(o);return{c(){n&&n.c(),e=D(),s&&s.c(),r=R()},l(l){n&&n.l(l),e=T(l),s&&s.l(l),r=R()},m(l,a){n&&n.m(l,a),_(l,e,a),s&&s.m(l,a),_(l,r,a),t=!0},p(l,[a]){l[2].length>0?n?(n.p(l,a),a&4&&c(n,1)):(n=he(l),n.c(),c(n,1),n.m(e.parentNode,e)):n&&(U(),p(n,1,1,()=>{n=null}),X()),l[1].templates||l[0]===L.Field?s?a&3&&c(s,1):(s=be(l),s.c(),c(s,1),s.m(r.parentNode,r)):s&&(U(),p(s,1,1,()=>{s=null}),X())},i(l){t||(c(n),c(s),t=!0)},o(l){p(n),p(s),t=!1},d(l){l&&(m(e),m(r)),n&&n.d(l),s&&s.d(l)}}}function Xt(o,e,r){let t,n,s,l=E,a=()=>(l(),l=ye(t,f=>r(1,s=f)),t);o.$$.on_destroy.push(()=>l());let{state:i}=e,{ctx:u}=e;return o.$$set=f=>{"state"in f&&r(4,i=f.state),"ctx"in f&&r(0,u=f.ctx)},o.$$.update=()=>{o.$$.dirty&16&&a(r(3,t=i.info)),o.$$.dirty&3&&r(2,n=s.isCloze&&u===L.Template?[]:s.unusedItems(u))},[u,s,n,t,i]}class ke extends j{constructor(e){super(),P(this,e,Xt,Ut,A,{state:4,ctx:0})}}function Yt(o){let e,r;return e=new Bt({props:{state:o[0]}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&1&&(s.state=t[0]),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Gt(o){let e,r,t,n;return e=new ke({props:{state:o[0],ctx:L.Field}}),t=new Ie({props:{state:o[0],ctx:L.Field}}),{c(){g(e.$$.fragment),r=D(),g(t.$$.fragment)},l(s){h(e.$$.fragment,s),r=T(s),h(t.$$.fragment,s)},m(s,l){b(e,s,l),_(s,r,l),b(t,s,l),n=!0},p(s,l){const a={};l&1&&(a.state=s[0]),e.$set(a);const i={};l&1&&(i.state=s[0]),t.$set(i)},i(s){n||(c(e.$$.fragment,s),c(t.$$.fragment,s),n=!0)},o(s){p(e.$$.fragment,s),p(t.$$.fragment,s),n=!1},d(s){s&&m(r),v(e,s),v(t,s)}}}function Jt(o){let e,r;return e=new q({props:{$$slots:{default:[Gt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&9&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Kt(o){let e,r;return e=new Ne({props:{title:Me(),$$slots:{default:[Jt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&9&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function Qt(o){let e,r,t=xe(qe())+"";return{c(){e=N("div"),r=new Qe(!1),this.h()},l(n){e=I(n,"DIV",{});var s=k(e);r=Ze(s,!1),s.forEach(m),this.h()},h(){r.a=null},m(n,s){_(n,e,s),r.m(t,e)},p:E,i:E,o:E,d(n){n&&m(e)}}}function Zt(o){let e,r;return e=new Ie({props:{state:o[0],ctx:L.Template}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&1&&(s.state=t[0]),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function xt(o){let e,r,t,n,s,l;e=new ke({props:{state:o[0],ctx:L.Template}});const a=[Zt,Qt],i=[];function u(f,$){return f[2].templates?0:1}return t=u(o),n=i[t]=a[t](o),{c(){g(e.$$.fragment),r=D(),n.c(),s=R()},l(f){h(e.$$.fragment,f),r=T(f),n.l(f),s=R()},m(f,$){b(e,f,$),_(f,r,$),i[t].m(f,$),_(f,s,$),l=!0},p(f,$){const d={};$&1&&(d.state=f[0]),e.$set(d);let S=t;t=u(f),t===S?i[t].p(f,$):(U(),p(i[S],1,1,()=>{i[S]=null}),X(),n=i[t],n?n.p(f,$):(n=i[t]=a[t](f),n.c()),c(n,1),n.m(s.parentNode,s))},i(f){l||(c(e.$$.fragment,f),c(n),l=!0)},o(f){p(e.$$.fragment,f),p(n),l=!1},d(f){f&&(m(r),m(s)),v(e,f),i[t].d(f)}}}function en(o){let e,r;return e=new q({props:{$$slots:{default:[xt]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&13&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function tn(o){let e,r;return e=new Ne({props:{title:Re(),$$slots:{default:[en]},$$scope:{ctx:o}}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,n){const s={};n&13&&(s.$$scope={dirty:n,ctx:t}),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function nn(o){let e,r,t,n,s,l;return e=new q({props:{$$slots:{default:[Kt]},$$scope:{ctx:o}}}),n=new q({props:{$$slots:{default:[tn]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),t=D(),s=N("div"),g(n.$$.fragment),this.h()},l(a){r=I(a,"DIV",{style:!0});var i=k(r);h(e.$$.fragment,i),t=T(a),s=I(a,"DIV",{style:!0});var u=k(s);h(n.$$.fragment,u),this.h()},h(){w(r,"display","contents"),w(r,"--cols",2),w(s,"display","contents"),w(s,"--cols",2)},m(a,i){_(a,r,i),b(e,r,null),_(a,t,i),_(a,s,i),b(n,s,null),l=!0},p(a,i){const u={};i&9&&(u.$$scope={dirty:i,ctx:a}),e.$set(u);const f={};i&13&&(f.$$scope={dirty:i,ctx:a}),n.$set(f)},i(a){l||(c(e.$$.fragment,a),c(n.$$.fragment,a),l=!0)},o(a){p(e.$$.fragment,a),p(n.$$.fragment,a),l=!1},d(a){a&&m(t),a&&e&&m(r),v(e,a),a&&n&&m(s),v(n,a)}}}function rn(o){let e,r,t,n,s,l;return e=new et({props:{breakpoint:"sm",$$slots:{default:[Yt]},$$scope:{ctx:o}}}),n=new x({props:{breakpoint:"sm",$$slots:{default:[nn]},$$scope:{ctx:o}}}),{c(){r=N("div"),g(e.$$.fragment),t=D(),s=N("div"),g(n.$$.fragment),this.h()},l(a){r=I(a,"DIV",{style:!0});var i=k(r);h(e.$$.fragment,i),t=T(a),s=I(a,"DIV",{style:!0});var u=k(s);h(n.$$.fragment,u),this.h()},h(){w(r,"display","contents"),w(r,"--gutter-block","0.5rem"),w(r,"--gutter-inline","0.25rem"),w(r,"--sticky-borders","0 0 1px"),w(s,"display","contents"),w(s,"--gutter-inline","0.25rem"),w(s,"--gutter-block","0.75rem")},m(a,i){_(a,r,i),b(e,r,null),_(a,t,i),_(a,s,i),b(n,s,null),l=!0},p(a,[i]){const u={};i&9&&(u.$$scope={dirty:i,ctx:a}),e.$set(u);const f={};i&13&&(f.$$scope={dirty:i,ctx:a}),n.$set(f)},i(a){l||(c(e.$$.fragment,a),c(n.$$.fragment,a),l=!0)},o(a){p(e.$$.fragment,a),p(n.$$.fragment,a),l=!1},d(a){a&&m(t),a&&e&&m(r),v(e,a),a&&n&&m(s),v(n,a)}}}function sn(o,e,r){let t,n,s=E,l=()=>(s(),s=ye(t,i=>r(2,n=i)),t);o.$$.on_destroy.push(()=>s());let{state:a}=e;return o.$$set=i=>{"state"in i&&r(0,a=i.state)},o.$$.update=()=>{o.$$.dirty&1&&l(r(1,t=a.info))},[a,t,n]}class ln extends j{constructor(e){super(),P(this,e,sn,rn,A,{state:0})}}function an(o){let e,r;return e=new ln({props:{state:o[0].state}}),{c(){g(e.$$.fragment)},l(t){h(e.$$.fragment,t)},m(t,n){b(e,t,n),r=!0},p(t,[n]){const s={};n&1&&(s.state=t[0].state),e.$set(s)},i(t){r||(c(e.$$.fragment,t),r=!0)},o(t){p(e.$$.fragment,t),r=!1},d(t){v(e,t)}}}function on(o,e,r){let{data:t}=e;return o.$$set=n=>{"data"in n&&r(0,t=n.data)},[t]}class Fn extends j{constructor(e){super(),P(this,e,on,an,A,{data:0})}}export{Fn as component,Tn as universal};

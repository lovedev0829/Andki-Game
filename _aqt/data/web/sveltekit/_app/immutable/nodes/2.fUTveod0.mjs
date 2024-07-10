import{b as wt,R as q}from"../chunks/backend.pzQSPd-R.mjs";import{S as he,i as _e,s as me,e as d,t as y,c as h,b as _,d as L,f as v,D as g,h as F,j as f,n as H,a3 as X,a as T,g as N,k as B,V as de,a4 as Se,B as Z,C as x,N as Ae,F as ee,v as K,r as O,H as te,q as dt,u as ht,l as bt}from"../chunks/Component.-XTVY6ph.mjs";import"../chunks/index.HrFqG6o2.mjs";import{p as $t}from"../chunks/stores.QbE_qdVv.mjs";import{C as St}from"../chunks/Container.T7flwP-u.mjs";import{R as _t}from"../chunks/Row.9I620FT8.mjs";import{P as Et,Q as Rt,R as Dt,S as kt,T as It,U as Vt,V as mt,W as Ct,X as Tt,Y as Nt,Z as gt,_ as yt,$ as Lt,a0 as Ft,a1 as At,a2 as Kt,a3 as Pt,a4 as jt,a5 as Ot,a6 as Bt,a7 as Gt,a8 as zt,a9 as Mt,aa as Wt,ab as qt,ac as Ht,ad as Ut,ae as Yt,af as Jt,ag as Qt,ah as Xt}from"../chunks/ftl.cKofWsqB.mjs";import{e as A}from"../chunks/each.mrBeHWFK.mjs";import{t as ve,D as Zt,T as pt}from"../chunks/time.KwyxY_gf.mjs";const xt=async({params:i})=>({info:await wt({cid:BigInt(i.cardId)})}),Cl=Object.freeze(Object.defineProperty({__proto__:null,load:xt},Symbol.toStringTag,{value:"Module"}));function el(i){let e,l=Et()+"",t;return{c(){e=d("div"),t=y(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=L(s,l),s.forEach(v),this.h()},h(){g(e,"class","card-info-placeholder svelte-1k3aa26")},m(a,s){F(a,e,s),f(e,t)},p:H,i:H,o:H,d(a){a&&v(e)}}}class tl extends he{constructor(e){super(),_e(this,e,null,el,me,{})}}function Xe(i,e,l){const t=i.slice();return t[4]=e[l],t}function Ze(i){let e,l,t=i[4].label+"",a,s,n,c=i[4].value+"",u,m;return{c(){e=d("tr"),l=d("th"),a=y(t),s=T(),n=d("td"),u=y(c),m=T(),this.h()},l(p){e=h(p,"TR",{});var w=_(e);l=h(w,"TH",{class:!0});var $=_(l);a=L($,t),$.forEach(v),s=N(w),n=h(w,"TD",{});var P=_(n);u=L(P,c),P.forEach(v),m=N(w),w.forEach(v),this.h()},h(){g(l,"class","align-start svelte-1ws7hzc")},m(p,w){F(p,e,w),f(e,l),f(l,a),f(e,s),f(e,n),f(n,u),f(e,m)},p(p,w){w&1&&t!==(t=p[4].label+"")&&B(a,t),w&1&&c!==(c=p[4].value+"")&&B(u,c)},d(p){p&&v(e)}}}function ll(i){let e,l=A(i[0]),t=[];for(let a=0;a<l.length;a+=1)t[a]=Ze(Xe(i,l,a));return{c(){e=d("table");for(let a=0;a<t.length;a+=1)t[a].c();this.h()},l(a){e=h(a,"TABLE",{class:!0});var s=_(e);for(let n=0;n<t.length;n+=1)t[n].l(s);s.forEach(v),this.h()},h(){g(e,"class","stats-table align-start svelte-1ws7hzc")},m(a,s){F(a,e,s);for(let n=0;n<t.length;n+=1)t[n]&&t[n].m(e,null)},p(a,[s]){if(s&1){l=A(a[0]);let n;for(n=0;n<l.length;n+=1){const c=Xe(a,l,n);t[n]?t[n].p(c,s):(t[n]=Ze(c),t[n].c(),t[n].m(e,null))}for(;n<t.length;n+=1)t[n].d(1);t.length=l.length}},i:H,o:H,d(a){a&&v(e),X(t,a)}}}function al(i,e,l){let{stats:t}=e;function a(c){return new pt(Number(c)).dateString()}function s(c){const u=[];if(u.push({label:Rt(),value:a(c.added)}),c.firstReview!=null&&u.push({label:Dt(),value:a(c.firstReview)}),c.latestReview!=null&&u.push({label:kt(),value:a(c.latestReview)}),c.dueDate!=null&&u.push({label:It(),value:a(c.dueDate)}),c.duePosition!=null&&u.push({label:Vt(),value:c.duePosition}),c.interval&&u.push({label:mt(),value:ve(c.interval*Zt)}),c.memoryState){let p=ve(c.memoryState.stability*86400,!1,!1);if(c.memoryState.stability>31){const $=c.memoryState.stability.toFixed(0);p+=` (${$})`}u.push({label:Ct(),value:p});const w=((c.memoryState.difficulty-1)/9*100).toFixed(0);if(u.push({label:Tt(),value:`${w}%`}),c.fsrsRetrievability){const $=(c.fsrsRetrievability*100).toFixed(0);u.push({label:Nt(),value:`${$}%`})}}else c.ease&&u.push({label:gt(),value:`${c.ease/10}%`});u.push({label:yt(),value:c.reviews}),u.push({label:Lt(),value:c.lapses}),c.totalSecs&&(u.push({label:Ft(),value:ve(c.averageSecs)}),u.push({label:At(),value:ve(c.totalSecs)})),u.push({label:Kt(),value:c.cardType}),u.push({label:Pt(),value:c.notetype});let m;if(c.originalDeck?m=`${c.deck} (${c.originalDeck})`:m=c.deck,u.push({label:jt(),value:m}),u.push({label:Ot(),value:c.preset}),u.push({label:Bt(),value:c.cardId}),u.push({label:Gt(),value:c.noteId}),c.customData){let p;try{const w=JSON.parse(c.customData);p=Object.entries(w).map(([$,P])=>`${$}=${P}`).join(" ")}catch{p=c.customData}u.push({label:zt(),value:p})}return u}let n;return i.$$set=c=>{"stats"in c&&l(1,t=c.stats)},i.$$.update=()=>{i.$$.dirty&2&&l(0,n=s(t))},[n,t]}class sl extends he{constructor(e){super(),_e(this,e,al,ll,me,{stats:1})}}function xe(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function et(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function tt(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function lt(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function at(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function st(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function rt(i){let e,l,t,a=Mt()+"",s,n,c,u,m,p,w=Wt()+"",$,P,j,Ee,G,le,Ke=qt()+"",Re,De,U,ke,z,ae,Pe=mt()+"",Ie,Ve,Y,Ce,M,se,je=gt()+"",Te,Ne,J,ye,W,re,Oe=Ht()+"",Le,Fe,Q,ne=A(i[1]),R=[];for(let o=0;o<ne.length;o+=1)R[o]=nt(st(i,ne,o));let ie=A(i[1]),D=[];for(let o=0;o<ie.length;o+=1)D[o]=it(at(i,ie,o));let ce=A(i[1]),k=[];for(let o=0;o<ce.length;o+=1)k[o]=ct(lt(i,ce,o));let oe=A(i[1]),I=[];for(let o=0;o<oe.length;o+=1)I[o]=ot(tt(i,oe,o));let ue=A(i[1]),V=[];for(let o=0;o<ue.length;o+=1)V[o]=ut(et(i,ue,o));let fe=A(i[1]),C=[];for(let o=0;o<fe.length;o+=1)C[o]=ft(xe(i,fe,o));return{c(){e=d("div"),l=d("div"),t=d("div"),s=y(a),n=T(),c=d("div");for(let o=0;o<R.length;o+=1)R[o].c();u=T(),m=d("div"),p=d("div"),$=y(w),P=T(),j=d("div");for(let o=0;o<D.length;o+=1)D[o].c();Ee=T(),G=d("div"),le=d("div"),Re=y(Ke),De=T(),U=d("div");for(let o=0;o<k.length;o+=1)k[o].c();ke=T(),z=d("div"),ae=d("div"),Ie=y(Pe),Ve=T(),Y=d("div");for(let o=0;o<I.length;o+=1)I[o].c();Ce=T(),M=d("div"),se=d("div"),Te=y(je),Ne=T(),J=d("div");for(let o=0;o<V.length;o+=1)V[o].c();ye=T(),W=d("div"),re=d("div"),Le=y(Oe),Fe=T(),Q=d("div");for(let o=0;o<C.length;o+=1)C[o].c();this.h()},l(o){e=h(o,"DIV",{class:!0});var b=_(e);l=h(b,"DIV",{class:!0});var r=_(l);t=h(r,"DIV",{class:!0});var E=_(t);s=L(E,a),E.forEach(v),n=N(r),c=h(r,"DIV",{class:!0});var Be=_(c);for(let S=0;S<R.length;S+=1)R[S].l(Be);Be.forEach(v),r.forEach(v),u=N(b),m=h(b,"DIV",{class:!0});var ge=_(m);p=h(ge,"DIV",{class:!0});var Ge=_(p);$=L(Ge,w),Ge.forEach(v),P=N(ge),j=h(ge,"DIV",{class:!0});var ze=_(j);for(let S=0;S<D.length;S+=1)D[S].l(ze);ze.forEach(v),ge.forEach(v),Ee=N(b),G=h(b,"DIV",{class:!0});var pe=_(G);le=h(pe,"DIV",{class:!0});var Me=_(le);Re=L(Me,Ke),Me.forEach(v),De=N(pe),U=h(pe,"DIV",{class:!0});var We=_(U);for(let S=0;S<k.length;S+=1)k[S].l(We);We.forEach(v),pe.forEach(v),ke=N(b),z=h(b,"DIV",{class:!0});var we=_(z);ae=h(we,"DIV",{class:!0});var qe=_(ae);Ie=L(qe,Pe),qe.forEach(v),Ve=N(we),Y=h(we,"DIV",{class:!0});var He=_(Y);for(let S=0;S<I.length;S+=1)I[S].l(He);He.forEach(v),we.forEach(v),Ce=N(b),M=h(b,"DIV",{class:!0});var be=_(M);se=h(be,"DIV",{class:!0});var Ue=_(se);Te=L(Ue,je),Ue.forEach(v),Ne=N(be),J=h(be,"DIV",{class:!0});var Ye=_(J);for(let S=0;S<V.length;S+=1)V[S].l(Ye);Ye.forEach(v),be.forEach(v),ye=N(b),W=h(b,"DIV",{class:!0});var $e=_(W);re=h($e,"DIV",{class:!0});var Je=_(re);Le=L(Je,Oe),Je.forEach(v),Fe=N($e),Q=h($e,"DIV",{class:!0});var Qe=_(Q);for(let S=0;S<C.length;S+=1)C[S].l(Qe);Qe.forEach(v),$e.forEach(v),b.forEach(v),this.h()},h(){g(t,"class","column-head svelte-1w0vs9e"),g(c,"class","column-content svelte-1w0vs9e"),g(l,"class","column svelte-1w0vs9e"),g(p,"class","column-head svelte-1w0vs9e"),g(j,"class","column-content svelte-1w0vs9e"),g(m,"class","column hidden-xs svelte-1w0vs9e"),g(le,"class","column-head svelte-1w0vs9e"),g(U,"class","column-content svelte-1w0vs9e"),g(G,"class","column svelte-1w0vs9e"),g(ae,"class","column-head svelte-1w0vs9e"),g(Y,"class","column-content right svelte-1w0vs9e"),g(z,"class","column svelte-1w0vs9e"),g(se,"class","column-head svelte-1w0vs9e"),g(J,"class","column-content svelte-1w0vs9e"),g(M,"class","column hidden-xs svelte-1w0vs9e"),g(re,"class","column-head svelte-1w0vs9e"),g(Q,"class","column-content right svelte-1w0vs9e"),g(W,"class","column svelte-1w0vs9e"),g(e,"class","revlog-table svelte-1w0vs9e")},m(o,b){F(o,e,b),f(e,l),f(l,t),f(t,s),f(l,n),f(l,c);for(let r=0;r<R.length;r+=1)R[r]&&R[r].m(c,null);f(e,u),f(e,m),f(m,p),f(p,$),f(m,P),f(m,j);for(let r=0;r<D.length;r+=1)D[r]&&D[r].m(j,null);f(e,Ee),f(e,G),f(G,le),f(le,Re),f(G,De),f(G,U);for(let r=0;r<k.length;r+=1)k[r]&&k[r].m(U,null);f(e,ke),f(e,z),f(z,ae),f(ae,Ie),f(z,Ve),f(z,Y);for(let r=0;r<I.length;r+=1)I[r]&&I[r].m(Y,null);f(e,Ce),f(e,M),f(M,se),f(se,Te),f(M,Ne),f(M,J);for(let r=0;r<V.length;r+=1)V[r]&&V[r].m(J,null);f(e,ye),f(e,W),f(W,re),f(re,Le),f(W,Fe),f(W,Q);for(let r=0;r<C.length;r+=1)C[r]&&C[r].m(Q,null)},p(o,b){if(b&2){ne=A(o[1]);let r;for(r=0;r<ne.length;r+=1){const E=st(o,ne,r);R[r]?R[r].p(E,b):(R[r]=nt(E),R[r].c(),R[r].m(c,null))}for(;r<R.length;r+=1)R[r].d(1);R.length=ne.length}if(b&2){ie=A(o[1]);let r;for(r=0;r<ie.length;r+=1){const E=at(o,ie,r);D[r]?D[r].p(E,b):(D[r]=it(E),D[r].c(),D[r].m(j,null))}for(;r<D.length;r+=1)D[r].d(1);D.length=ie.length}if(b&2){ce=A(o[1]);let r;for(r=0;r<ce.length;r+=1){const E=lt(o,ce,r);k[r]?k[r].p(E,b):(k[r]=ct(E),k[r].c(),k[r].m(U,null))}for(;r<k.length;r+=1)k[r].d(1);k.length=ce.length}if(b&2){oe=A(o[1]);let r;for(r=0;r<oe.length;r+=1){const E=tt(o,oe,r);I[r]?I[r].p(E,b):(I[r]=ot(E),I[r].c(),I[r].m(Y,null))}for(;r<I.length;r+=1)I[r].d(1);I.length=oe.length}if(b&2){ue=A(o[1]);let r;for(r=0;r<ue.length;r+=1){const E=et(o,ue,r);V[r]?V[r].p(E,b):(V[r]=ut(E),V[r].c(),V[r].m(J,null))}for(;r<V.length;r+=1)V[r].d(1);V.length=ue.length}if(b&2){fe=A(o[1]);let r;for(r=0;r<fe.length;r+=1){const E=xe(o,fe,r);C[r]?C[r].p(E,b):(C[r]=ft(E),C[r].c(),C[r].m(Q,null))}for(;r<C.length;r+=1)C[r].d(1);C.length=fe.length}},d(o){o&&v(e),X(R,o),X(D,o),X(k,o),X(I,o),X(V,o),X(C,o)}}}function nt(i){let e,l,t=i[5].date+"",a,s,n,c,u=i[5].time+"",m,p;return{c(){e=d("div"),l=d("b"),a=y(t),s=T(),n=d("span"),c=y("@ "),m=y(u),p=T(),this.h()},l(w){e=h(w,"DIV",{class:!0});var $=_(e);l=h($,"B",{});var P=_(l);a=L(P,t),P.forEach(v),s=N($),n=h($,"SPAN",{class:!0});var j=_(n);c=L(j,"@ "),m=L(j,u),j.forEach(v),p=N($),$.forEach(v),this.h()},h(){g(n,"class","hidden-xs svelte-1w0vs9e"),g(e,"class","svelte-1w0vs9e")},m(w,$){F(w,e,$),f(e,l),f(l,a),f(e,s),f(e,n),f(n,c),f(n,m),f(e,p)},p(w,$){$&2&&t!==(t=w[5].date+"")&&B(a,t),$&2&&u!==(u=w[5].time+"")&&B(m,u)},d(w){w&&v(e)}}}function it(i){let e,l=i[5].reviewKind+"",t,a,s;return{c(){e=d("div"),t=y(l),a=T(),this.h()},l(n){e=h(n,"DIV",{class:!0});var c=_(e);t=L(c,l),a=N(c),c.forEach(v),this.h()},h(){g(e,"class",s=Se(i[5].reviewKindClass)+" svelte-1w0vs9e")},m(n,c){F(n,e,c),f(e,t),f(e,a)},p(n,c){c&2&&l!==(l=n[5].reviewKind+"")&&B(t,l),c&2&&s!==(s=Se(n[5].reviewKindClass)+" svelte-1w0vs9e")&&g(e,"class",s)},d(n){n&&v(e)}}}function ct(i){let e,l=i[5].rating+"",t,a;return{c(){e=d("div"),t=y(l),this.h()},l(s){e=h(s,"DIV",{class:!0});var n=_(e);t=L(n,l),n.forEach(v),this.h()},h(){g(e,"class",a=Se(i[5].ratingClass)+" svelte-1w0vs9e")},m(s,n){F(s,e,n),f(e,t)},p(s,n){n&2&&l!==(l=s[5].rating+"")&&B(t,l),n&2&&a!==(a=Se(s[5].ratingClass)+" svelte-1w0vs9e")&&g(e,"class",a)},d(s){s&&v(e)}}}function ot(i){let e,l=i[5].interval+"",t;return{c(){e=d("div"),t=y(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=L(s,l),s.forEach(v),this.h()},h(){g(e,"class","svelte-1w0vs9e")},m(a,s){F(a,e,s),f(e,t)},p(a,s){s&2&&l!==(l=a[5].interval+"")&&B(t,l)},d(a){a&&v(e)}}}function ut(i){let e,l=i[5].ease+"",t;return{c(){e=d("div"),t=y(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=L(s,l),s.forEach(v),this.h()},h(){g(e,"class","svelte-1w0vs9e")},m(a,s){F(a,e,s),f(e,t)},p(a,s){s&2&&l!==(l=a[5].ease+"")&&B(t,l)},d(a){a&&v(e)}}}function ft(i){let e,l=i[5].takenSecs+"",t;return{c(){e=d("div"),t=y(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=L(s,l),s.forEach(v),this.h()},h(){g(e,"class","svelte-1w0vs9e")},m(a,s){F(a,e,s),f(e,t)},p(a,s){s&2&&l!==(l=a[5].takenSecs+"")&&B(t,l)},d(a){a&&v(e)}}}function rl(i){let e,l=i[0].length>0&&rt(i);return{c(){l&&l.c(),e=de()},l(t){l&&l.l(t),e=de()},m(t,a){l&&l.m(t,a),F(t,e,a)},p(t,[a]){t[0].length>0?l?l.p(t,a):(l=rt(t),l.c(),l.m(e.parentNode,e)):l&&(l.d(1),l=null)},i:H,o:H,d(t){t&&v(e),l&&l.d(t)}}}function nl(i){return i.buttonChosen===1?"revlog-ease1":""}function il(i){if(i===0)return"";const e=i/10;return e<=110?`D:${(e-10).toFixed(0)}%`:`${e.toFixed(0)}%`}function cl(i,e,l){let t,{revlog:a}=e;function s(u){switch(u.reviewKind){case q.LEARNING:return"revlog-learn";case q.REVIEW:return"revlog-review";case q.RELEARNING:return"revlog-relearn"}return""}function n(u){switch(u.reviewKind){case q.LEARNING:return Xt();case q.REVIEW:return Qt();case q.RELEARNING:return Jt();case q.FILTERED:return Yt();case q.MANUAL:return Ut()}}function c(u){const m=new pt(Number(u.time));return{date:m.dateString(),time:m.timeString(),reviewKind:n(u),reviewKindClass:s(u),rating:u.buttonChosen,ratingClass:nl(u),interval:ve(u.interval),ease:il(u.ease),takenSecs:ve(u.takenSecs,!0)}}return i.$$set=u=>{"revlog"in u&&l(0,a=u.revlog)},i.$$.update=()=>{i.$$.dirty&1&&l(1,t=a.map(c))},[a,t]}class ol extends he{constructor(e){super(),_e(this,e,cl,rl,me,{revlog:0})}}function ul(i){let e,l;return e=new tl({}),{c(){Z(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p:H,i(t){l||(K(e.$$.fragment,t),l=!0)},o(t){O(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function fl(i){let e,l,t,a;e=new _t({props:{$$slots:{default:[vl]},$$scope:{ctx:i}}});let s=i[1]&&vt(i);return{c(){Z(e.$$.fragment),l=T(),s&&s.c(),t=de()},l(n){x(e.$$.fragment,n),l=N(n),s&&s.l(n),t=de()},m(n,c){ee(e,n,c),F(n,l,c),s&&s.m(n,c),F(n,t,c),a=!0},p(n,c){const u={};c&5&&(u.$$scope={dirty:c,ctx:n}),e.$set(u),n[1]?s?(s.p(n,c),c&2&&K(s,1)):(s=vt(n),s.c(),K(s,1),s.m(t.parentNode,t)):s&&(dt(),O(s,1,1,()=>{s=null}),ht())},i(n){a||(K(e.$$.fragment,n),K(s),a=!0)},o(n){O(e.$$.fragment,n),O(s),a=!1},d(n){n&&(v(l),v(t)),te(e,n),s&&s.d(n)}}}function vl(i){let e,l;return e=new sl({props:{stats:i[0]}}),{c(){Z(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&1&&(s.stats=t[0]),e.$set(s)},i(t){l||(K(e.$$.fragment,t),l=!0)},o(t){O(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function vt(i){let e,l;return e=new _t({props:{$$slots:{default:[dl]},$$scope:{ctx:i}}}),{c(){Z(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&5&&(s.$$scope={dirty:a,ctx:t}),e.$set(s)},i(t){l||(K(e.$$.fragment,t),l=!0)},o(t){O(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function dl(i){let e,l;return e=new ol({props:{revlog:i[0].revlog}}),{c(){Z(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&1&&(s.revlog=t[0].revlog),e.$set(s)},i(t){l||(K(e.$$.fragment,t),l=!0)},o(t){O(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function hl(i){let e,l,t,a;const s=[fl,ul],n=[];function c(u,m){return u[0]?0:1}return e=c(i),l=n[e]=s[e](i),{c(){l.c(),t=de()},l(u){l.l(u),t=de()},m(u,m){n[e].m(u,m),F(u,t,m),a=!0},p(u,m){let p=e;e=c(u),e===p?n[e].p(u,m):(dt(),O(n[p],1,1,()=>{n[p]=null}),ht(),l=n[e],l?l.p(u,m):(l=n[e]=s[e](u),l.c()),K(l,1),l.m(t.parentNode,t))},i(u){a||(K(l),a=!0)},o(u){O(l),a=!1},d(u){u&&v(t),n[e].d(u)}}}function _l(i){let e,l,t;return e=new St({props:{breakpoint:"md",$$slots:{default:[hl]},$$scope:{ctx:i}}}),{c(){l=d("div"),Z(e.$$.fragment),this.h()},l(a){l=h(a,"DIV",{style:!0});var s=_(l);x(e.$$.fragment,s),this.h()},h(){Ae(l,"display","contents"),Ae(l,"--gutter-inline","1rem"),Ae(l,"--gutter-block","0.5rem")},m(a,s){F(a,l,s),ee(e,l,null),t=!0},p(a,[s]){const n={};s&7&&(n.$$scope={dirty:s,ctx:a}),e.$set(n)},i(a){t||(K(e.$$.fragment,a),t=!0)},o(a){O(e.$$.fragment,a),t=!1},d(a){a&&e&&v(l),te(e,a)}}}function ml(i,e,l){let{stats:t=null}=e,{showRevlog:a=!0}=e;return i.$$set=s=>{"stats"in s&&l(0,t=s.stats),"showRevlog"in s&&l(1,a=s.showRevlog)},[t,a]}class gl extends he{constructor(e){super(),_e(this,e,ml,_l,me,{stats:0,showRevlog:1})}}function pl(i){let e,l;return e=new gl({props:{stats:i[0].info,showRevlog:i[1]}}),{c(){Z(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,[a]){const s={};a&1&&(s.stats=t[0].info),e.$set(s)},i(t){l||(K(e.$$.fragment,t),l=!0)},o(t){O(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function wl(i,e,l){let t;bt(i,$t,n=>l(2,t=n));let{data:a}=e;const s=t.url.searchParams.get("revlog")!=="0";return i.$$set=n=>{"data"in n&&l(0,a=n.data)},[a,s]}class Tl extends he{constructor(e){super(),_e(this,e,wl,pl,me,{data:0})}}export{Tl as component,Cl as universal};

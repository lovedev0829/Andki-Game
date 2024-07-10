import{d as bt,R as M}from"../chunks/backend.dXWO455a.mjs";import{S as he,i as _e,s as me,e as v,t as N,c as h,b as _,d as y,f as d,F as g,h as L,j as u,n as U,a3 as Z,a as C,g as T,k as O,W as ve,a4 as Se,B as Q,C as x,N as Fe,D as ee,v as A,r as j,E as te,q as vt,u as ht,l as $t}from"../chunks/Component.C0CSGRj9.mjs";import"../chunks/index.HrFqG6o2.mjs";import{p as wt}from"../chunks/stores.ruPdQHV4.mjs";import{C as St}from"../chunks/Container.gOvVoQ_U.mjs";import{R as _t}from"../chunks/Row.xEM4s8hj.mjs";import{S as Et,T as Rt,U as kt,V as Dt,W as It,X as qt,Y as mt,Z as Vt,_ as Ct,$ as Tt,a0 as gt,a1 as Nt,a2 as yt,a3 as Lt,a4 as Ft,a5 as At,a6 as Kt,a7 as Pt,a8 as jt,a9 as Ot,aa as Bt,ab as Gt,ac as Wt,ad as zt,ae as Mt,af as Ut,ag as Yt,ah as Ht,ai as Jt,aj as Xt,ak as Zt}from"../chunks/ftl.IxHLS1AB.mjs";import{e as F}from"../chunks/each.AJyTDN0I.mjs";import{t as de,D as Qt,T as pt}from"../chunks/time.dB5-GOAi.mjs";const xt=async({params:i})=>({info:await bt({cid:BigInt(i.cardId)})}),Vl=Object.freeze(Object.defineProperty({__proto__:null,load:xt},Symbol.toStringTag,{value:"Module"}));function el(i){let e,l=Et()+"",t;return{c(){e=v("div"),t=N(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=y(s,l),s.forEach(d),this.h()},h(){g(e,"class","card-info-placeholder svelte-1k3aa26")},m(a,s){L(a,e,s),u(e,t)},p:U,i:U,o:U,d(a){a&&d(e)}}}class tl extends he{constructor(e){super(),_e(this,e,null,el,me,{})}}function Ze(i,e,l){const t=i.slice();return t[4]=e[l],t}function Qe(i){let e,l,t=i[4].label+"",a,s,n,c=i[4].value+"",f,m;return{c(){e=v("tr"),l=v("th"),a=N(t),s=C(),n=v("td"),f=N(c),m=C(),this.h()},l(p){e=h(p,"TR",{});var b=_(e);l=h(b,"TH",{class:!0});var w=_(l);a=y(w,t),w.forEach(d),s=T(b),n=h(b,"TD",{});var K=_(n);f=y(K,c),K.forEach(d),m=T(b),b.forEach(d),this.h()},h(){g(l,"class","align-start svelte-1ws7hzc")},m(p,b){L(p,e,b),u(e,l),u(l,a),u(e,s),u(e,n),u(n,f),u(e,m)},p(p,b){b&1&&t!==(t=p[4].label+"")&&O(a,t),b&1&&c!==(c=p[4].value+"")&&O(f,c)},d(p){p&&d(e)}}}function ll(i){let e,l=F(i[0]),t=[];for(let a=0;a<l.length;a+=1)t[a]=Qe(Ze(i,l,a));return{c(){e=v("table");for(let a=0;a<t.length;a+=1)t[a].c();this.h()},l(a){e=h(a,"TABLE",{class:!0});var s=_(e);for(let n=0;n<t.length;n+=1)t[n].l(s);s.forEach(d),this.h()},h(){g(e,"class","stats-table align-start svelte-1ws7hzc")},m(a,s){L(a,e,s);for(let n=0;n<t.length;n+=1)t[n]&&t[n].m(e,null)},p(a,[s]){if(s&1){l=F(a[0]);let n;for(n=0;n<l.length;n+=1){const c=Ze(a,l,n);t[n]?t[n].p(c,s):(t[n]=Qe(c),t[n].c(),t[n].m(e,null))}for(;n<t.length;n+=1)t[n].d(1);t.length=l.length}},i:U,o:U,d(a){a&&d(e),Z(t,a)}}}function al(i,e,l){let{stats:t}=e;function a(c){return new pt(Number(c)).dateString()}function s(c){const f=[];if(f.push({label:Rt(),value:a(c.added)}),c.firstReview!=null&&f.push({label:kt(),value:a(c.firstReview)}),c.latestReview!=null&&f.push({label:Dt(),value:a(c.latestReview)}),c.dueDate!=null&&f.push({label:It(),value:a(c.dueDate)}),c.duePosition!=null&&f.push({label:qt(),value:c.duePosition}),c.interval&&f.push({label:mt(),value:de(c.interval*Qt)}),c.memoryState){let p=de(c.memoryState.stability*86400,!1,!1);if(c.memoryState.stability>31){const w=c.memoryState.stability.toFixed(0);p+=` (${w})`}f.push({label:Vt(),value:p});const b=((c.memoryState.difficulty-1)/9*100).toFixed(0);if(f.push({label:Ct(),value:`${b}%`}),c.fsrsRetrievability){const w=(c.fsrsRetrievability*100).toFixed(0);f.push({label:Tt(),value:`${w}%`})}}else c.ease&&f.push({label:gt(),value:`${c.ease/10}%`});f.push({label:Nt(),value:c.reviews}),f.push({label:yt(),value:c.lapses}),c.totalSecs&&(f.push({label:Lt(),value:de(c.averageSecs)}),f.push({label:Ft(),value:de(c.totalSecs)})),f.push({label:At(),value:c.cardType}),f.push({label:Kt(),value:c.notetype});let m;if(c.originalDeck?m=`${c.deck} (${c.originalDeck})`:m=c.deck,f.push({label:Pt(),value:m}),f.push({label:jt(),value:c.preset}),f.push({label:Ot(),value:c.cardId}),f.push({label:Bt(),value:c.noteId}),c.customData){let p;try{const b=JSON.parse(c.customData);p=Object.entries(b).map(([w,K])=>`${w}=${K}`).join(" ")}catch{p=c.customData}f.push({label:Gt(),value:p})}return f}let n;return i.$$set=c=>{"stats"in c&&l(1,t=c.stats)},i.$$.update=()=>{i.$$.dirty&2&&l(0,n=s(t))},[n,t]}class sl extends he{constructor(e){super(),_e(this,e,al,ll,me,{stats:1})}}function xe(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function et(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function tt(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function lt(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function at(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function st(i,e,l){const t=i.slice();return t[5]=e[l],t[7]=l,t}function rt(i){let e,l,t,a=Wt()+"",s,n,c,f,m,p,b=zt()+"",w,K,P,Ee,B,le,Ae=Mt()+"",Re,ke,Y,De,G,ae,Ke=mt()+"",Ie,qe,H,Ve,W,se,Pe=gt()+"",Ce,Te,J,Ne,z,re,je=Ut()+"",ye,Le,X,ne=F(i[1]),R=[];for(let o=0;o<ne.length;o+=1)R[o]=nt(st(i,ne,o));let ie=F(i[1]),k=[];for(let o=0;o<ie.length;o+=1)k[o]=it(at(i,ie,o));let ce=F(i[1]),D=[];for(let o=0;o<ce.length;o+=1)D[o]=ct(lt(i,ce,o));let oe=F(i[1]),I=[];for(let o=0;o<oe.length;o+=1)I[o]=ot(tt(i,oe,o));let fe=F(i[1]),q=[];for(let o=0;o<fe.length;o+=1)q[o]=ft(et(i,fe,o));let ue=F(i[1]),V=[];for(let o=0;o<ue.length;o+=1)V[o]=ut(xe(i,ue,o));return{c(){e=v("div"),l=v("div"),t=v("div"),s=N(a),n=C(),c=v("div");for(let o=0;o<R.length;o+=1)R[o].c();f=C(),m=v("div"),p=v("div"),w=N(b),K=C(),P=v("div");for(let o=0;o<k.length;o+=1)k[o].c();Ee=C(),B=v("div"),le=v("div"),Re=N(Ae),ke=C(),Y=v("div");for(let o=0;o<D.length;o+=1)D[o].c();De=C(),G=v("div"),ae=v("div"),Ie=N(Ke),qe=C(),H=v("div");for(let o=0;o<I.length;o+=1)I[o].c();Ve=C(),W=v("div"),se=v("div"),Ce=N(Pe),Te=C(),J=v("div");for(let o=0;o<q.length;o+=1)q[o].c();Ne=C(),z=v("div"),re=v("div"),ye=N(je),Le=C(),X=v("div");for(let o=0;o<V.length;o+=1)V[o].c();this.h()},l(o){e=h(o,"DIV",{class:!0});var $=_(e);l=h($,"DIV",{class:!0});var r=_(l);t=h(r,"DIV",{class:!0});var E=_(t);s=y(E,a),E.forEach(d),n=T(r),c=h(r,"DIV",{class:!0});var Oe=_(c);for(let S=0;S<R.length;S+=1)R[S].l(Oe);Oe.forEach(d),r.forEach(d),f=T($),m=h($,"DIV",{class:!0});var ge=_(m);p=h(ge,"DIV",{class:!0});var Be=_(p);w=y(Be,b),Be.forEach(d),K=T(ge),P=h(ge,"DIV",{class:!0});var Ge=_(P);for(let S=0;S<k.length;S+=1)k[S].l(Ge);Ge.forEach(d),ge.forEach(d),Ee=T($),B=h($,"DIV",{class:!0});var pe=_(B);le=h(pe,"DIV",{class:!0});var We=_(le);Re=y(We,Ae),We.forEach(d),ke=T(pe),Y=h(pe,"DIV",{class:!0});var ze=_(Y);for(let S=0;S<D.length;S+=1)D[S].l(ze);ze.forEach(d),pe.forEach(d),De=T($),G=h($,"DIV",{class:!0});var be=_(G);ae=h(be,"DIV",{class:!0});var Me=_(ae);Ie=y(Me,Ke),Me.forEach(d),qe=T(be),H=h(be,"DIV",{class:!0});var Ue=_(H);for(let S=0;S<I.length;S+=1)I[S].l(Ue);Ue.forEach(d),be.forEach(d),Ve=T($),W=h($,"DIV",{class:!0});var $e=_(W);se=h($e,"DIV",{class:!0});var Ye=_(se);Ce=y(Ye,Pe),Ye.forEach(d),Te=T($e),J=h($e,"DIV",{class:!0});var He=_(J);for(let S=0;S<q.length;S+=1)q[S].l(He);He.forEach(d),$e.forEach(d),Ne=T($),z=h($,"DIV",{class:!0});var we=_(z);re=h(we,"DIV",{class:!0});var Je=_(re);ye=y(Je,je),Je.forEach(d),Le=T(we),X=h(we,"DIV",{class:!0});var Xe=_(X);for(let S=0;S<V.length;S+=1)V[S].l(Xe);Xe.forEach(d),we.forEach(d),$.forEach(d),this.h()},h(){g(t,"class","column-head svelte-1bf093q"),g(c,"class","column-content svelte-1bf093q"),g(l,"class","column svelte-1bf093q"),g(p,"class","column-head svelte-1bf093q"),g(P,"class","column-content svelte-1bf093q"),g(m,"class","column hidden-xs svelte-1bf093q"),g(le,"class","column-head svelte-1bf093q"),g(Y,"class","column-content svelte-1bf093q"),g(B,"class","column svelte-1bf093q"),g(ae,"class","column-head svelte-1bf093q"),g(H,"class","column-content right svelte-1bf093q"),g(G,"class","column svelte-1bf093q"),g(se,"class","column-head svelte-1bf093q"),g(J,"class","column-content svelte-1bf093q"),g(W,"class","column hidden-xs svelte-1bf093q"),g(re,"class","column-head svelte-1bf093q"),g(X,"class","column-content right svelte-1bf093q"),g(z,"class","column svelte-1bf093q"),g(e,"class","revlog-table svelte-1bf093q")},m(o,$){L(o,e,$),u(e,l),u(l,t),u(t,s),u(l,n),u(l,c);for(let r=0;r<R.length;r+=1)R[r]&&R[r].m(c,null);u(e,f),u(e,m),u(m,p),u(p,w),u(m,K),u(m,P);for(let r=0;r<k.length;r+=1)k[r]&&k[r].m(P,null);u(e,Ee),u(e,B),u(B,le),u(le,Re),u(B,ke),u(B,Y);for(let r=0;r<D.length;r+=1)D[r]&&D[r].m(Y,null);u(e,De),u(e,G),u(G,ae),u(ae,Ie),u(G,qe),u(G,H);for(let r=0;r<I.length;r+=1)I[r]&&I[r].m(H,null);u(e,Ve),u(e,W),u(W,se),u(se,Ce),u(W,Te),u(W,J);for(let r=0;r<q.length;r+=1)q[r]&&q[r].m(J,null);u(e,Ne),u(e,z),u(z,re),u(re,ye),u(z,Le),u(z,X);for(let r=0;r<V.length;r+=1)V[r]&&V[r].m(X,null)},p(o,$){if($&2){ne=F(o[1]);let r;for(r=0;r<ne.length;r+=1){const E=st(o,ne,r);R[r]?R[r].p(E,$):(R[r]=nt(E),R[r].c(),R[r].m(c,null))}for(;r<R.length;r+=1)R[r].d(1);R.length=ne.length}if($&2){ie=F(o[1]);let r;for(r=0;r<ie.length;r+=1){const E=at(o,ie,r);k[r]?k[r].p(E,$):(k[r]=it(E),k[r].c(),k[r].m(P,null))}for(;r<k.length;r+=1)k[r].d(1);k.length=ie.length}if($&2){ce=F(o[1]);let r;for(r=0;r<ce.length;r+=1){const E=lt(o,ce,r);D[r]?D[r].p(E,$):(D[r]=ct(E),D[r].c(),D[r].m(Y,null))}for(;r<D.length;r+=1)D[r].d(1);D.length=ce.length}if($&2){oe=F(o[1]);let r;for(r=0;r<oe.length;r+=1){const E=tt(o,oe,r);I[r]?I[r].p(E,$):(I[r]=ot(E),I[r].c(),I[r].m(H,null))}for(;r<I.length;r+=1)I[r].d(1);I.length=oe.length}if($&2){fe=F(o[1]);let r;for(r=0;r<fe.length;r+=1){const E=et(o,fe,r);q[r]?q[r].p(E,$):(q[r]=ft(E),q[r].c(),q[r].m(J,null))}for(;r<q.length;r+=1)q[r].d(1);q.length=fe.length}if($&2){ue=F(o[1]);let r;for(r=0;r<ue.length;r+=1){const E=xe(o,ue,r);V[r]?V[r].p(E,$):(V[r]=ut(E),V[r].c(),V[r].m(X,null))}for(;r<V.length;r+=1)V[r].d(1);V.length=ue.length}},d(o){o&&d(e),Z(R,o),Z(k,o),Z(D,o),Z(I,o),Z(q,o),Z(V,o)}}}function nt(i){let e,l,t=i[5].date+"",a,s,n,c,f=i[5].time+"",m,p;return{c(){e=v("div"),l=v("b"),a=N(t),s=C(),n=v("span"),c=N("@ "),m=N(f),p=C(),this.h()},l(b){e=h(b,"DIV",{class:!0});var w=_(e);l=h(w,"B",{});var K=_(l);a=y(K,t),K.forEach(d),s=T(w),n=h(w,"SPAN",{class:!0});var P=_(n);c=y(P,"@ "),m=y(P,f),P.forEach(d),p=T(w),w.forEach(d),this.h()},h(){g(n,"class","hidden-xs svelte-1bf093q"),g(e,"class","svelte-1bf093q")},m(b,w){L(b,e,w),u(e,l),u(l,a),u(e,s),u(e,n),u(n,c),u(n,m),u(e,p)},p(b,w){w&2&&t!==(t=b[5].date+"")&&O(a,t),w&2&&f!==(f=b[5].time+"")&&O(m,f)},d(b){b&&d(e)}}}function it(i){let e,l=i[5].reviewKind+"",t,a,s;return{c(){e=v("div"),t=N(l),a=C(),this.h()},l(n){e=h(n,"DIV",{class:!0});var c=_(e);t=y(c,l),a=T(c),c.forEach(d),this.h()},h(){g(e,"class",s=Se(i[5].reviewKindClass)+" svelte-1bf093q")},m(n,c){L(n,e,c),u(e,t),u(e,a)},p(n,c){c&2&&l!==(l=n[5].reviewKind+"")&&O(t,l),c&2&&s!==(s=Se(n[5].reviewKindClass)+" svelte-1bf093q")&&g(e,"class",s)},d(n){n&&d(e)}}}function ct(i){let e,l=i[5].rating+"",t,a;return{c(){e=v("div"),t=N(l),this.h()},l(s){e=h(s,"DIV",{class:!0});var n=_(e);t=y(n,l),n.forEach(d),this.h()},h(){g(e,"class",a=Se(i[5].ratingClass)+" svelte-1bf093q")},m(s,n){L(s,e,n),u(e,t)},p(s,n){n&2&&l!==(l=s[5].rating+"")&&O(t,l),n&2&&a!==(a=Se(s[5].ratingClass)+" svelte-1bf093q")&&g(e,"class",a)},d(s){s&&d(e)}}}function ot(i){let e,l=i[5].interval+"",t;return{c(){e=v("div"),t=N(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=y(s,l),s.forEach(d),this.h()},h(){g(e,"class","svelte-1bf093q")},m(a,s){L(a,e,s),u(e,t)},p(a,s){s&2&&l!==(l=a[5].interval+"")&&O(t,l)},d(a){a&&d(e)}}}function ft(i){let e,l=i[5].ease+"",t;return{c(){e=v("div"),t=N(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=y(s,l),s.forEach(d),this.h()},h(){g(e,"class","svelte-1bf093q")},m(a,s){L(a,e,s),u(e,t)},p(a,s){s&2&&l!==(l=a[5].ease+"")&&O(t,l)},d(a){a&&d(e)}}}function ut(i){let e,l=i[5].takenSecs+"",t;return{c(){e=v("div"),t=N(l),this.h()},l(a){e=h(a,"DIV",{class:!0});var s=_(e);t=y(s,l),s.forEach(d),this.h()},h(){g(e,"class","svelte-1bf093q")},m(a,s){L(a,e,s),u(e,t)},p(a,s){s&2&&l!==(l=a[5].takenSecs+"")&&O(t,l)},d(a){a&&d(e)}}}function rl(i){let e,l=i[0].length>0&&rt(i);return{c(){l&&l.c(),e=ve()},l(t){l&&l.l(t),e=ve()},m(t,a){l&&l.m(t,a),L(t,e,a)},p(t,[a]){t[0].length>0?l?l.p(t,a):(l=rt(t),l.c(),l.m(e.parentNode,e)):l&&(l.d(1),l=null)},i:U,o:U,d(t){t&&d(e),l&&l.d(t)}}}function nl(i){return i.buttonChosen===1?"revlog-ease1":""}function il(i){if(i===0)return"";const e=i/10;return e<=110?`D:${(e-10).toFixed(0)}%`:`${e.toFixed(0)}%`}function cl(i,e,l){let t,{revlog:a}=e;function s(f){switch(f.reviewKind){case M.LEARNING:return"revlog-learn";case M.REVIEW:return"revlog-review";case M.RELEARNING:return"revlog-relearn"}return""}function n(f){switch(f.reviewKind){case M.LEARNING:return Zt();case M.REVIEW:return Xt();case M.RELEARNING:return Jt();case M.FILTERED:return Ht();case M.MANUAL:return Yt()}}function c(f){const m=new pt(Number(f.time));return{date:m.dateString(),time:m.timeString(),reviewKind:n(f),reviewKindClass:s(f),rating:f.buttonChosen,ratingClass:nl(f),interval:de(f.interval),ease:il(f.ease),takenSecs:de(f.takenSecs,!0)}}return i.$$set=f=>{"revlog"in f&&l(0,a=f.revlog)},i.$$.update=()=>{i.$$.dirty&1&&l(1,t=a.map(c))},[a,t]}class ol extends he{constructor(e){super(),_e(this,e,cl,rl,me,{revlog:0})}}function fl(i){let e,l;return e=new tl({}),{c(){Q(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p:U,i(t){l||(A(e.$$.fragment,t),l=!0)},o(t){j(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function ul(i){let e,l,t,a;e=new _t({props:{$$slots:{default:[dl]},$$scope:{ctx:i}}});let s=i[1]&&dt(i);return{c(){Q(e.$$.fragment),l=C(),s&&s.c(),t=ve()},l(n){x(e.$$.fragment,n),l=T(n),s&&s.l(n),t=ve()},m(n,c){ee(e,n,c),L(n,l,c),s&&s.m(n,c),L(n,t,c),a=!0},p(n,c){const f={};c&5&&(f.$$scope={dirty:c,ctx:n}),e.$set(f),n[1]?s?(s.p(n,c),c&2&&A(s,1)):(s=dt(n),s.c(),A(s,1),s.m(t.parentNode,t)):s&&(vt(),j(s,1,1,()=>{s=null}),ht())},i(n){a||(A(e.$$.fragment,n),A(s),a=!0)},o(n){j(e.$$.fragment,n),j(s),a=!1},d(n){n&&(d(l),d(t)),te(e,n),s&&s.d(n)}}}function dl(i){let e,l;return e=new sl({props:{stats:i[0]}}),{c(){Q(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&1&&(s.stats=t[0]),e.$set(s)},i(t){l||(A(e.$$.fragment,t),l=!0)},o(t){j(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function dt(i){let e,l;return e=new _t({props:{$$slots:{default:[vl]},$$scope:{ctx:i}}}),{c(){Q(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&5&&(s.$$scope={dirty:a,ctx:t}),e.$set(s)},i(t){l||(A(e.$$.fragment,t),l=!0)},o(t){j(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function vl(i){let e,l;return e=new ol({props:{revlog:i[0].revlog}}),{c(){Q(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,a){const s={};a&1&&(s.revlog=t[0].revlog),e.$set(s)},i(t){l||(A(e.$$.fragment,t),l=!0)},o(t){j(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function hl(i){let e,l,t,a;const s=[ul,fl],n=[];function c(f,m){return f[0]?0:1}return e=c(i),l=n[e]=s[e](i),{c(){l.c(),t=ve()},l(f){l.l(f),t=ve()},m(f,m){n[e].m(f,m),L(f,t,m),a=!0},p(f,m){let p=e;e=c(f),e===p?n[e].p(f,m):(vt(),j(n[p],1,1,()=>{n[p]=null}),ht(),l=n[e],l?l.p(f,m):(l=n[e]=s[e](f),l.c()),A(l,1),l.m(t.parentNode,t))},i(f){a||(A(l),a=!0)},o(f){j(l),a=!1},d(f){f&&d(t),n[e].d(f)}}}function _l(i){let e,l,t;return e=new St({props:{breakpoint:"md",$$slots:{default:[hl]},$$scope:{ctx:i}}}),{c(){l=v("div"),Q(e.$$.fragment),this.h()},l(a){l=h(a,"DIV",{style:!0});var s=_(l);x(e.$$.fragment,s),this.h()},h(){Fe(l,"display","contents"),Fe(l,"--gutter-inline","1rem"),Fe(l,"--gutter-block","0.5rem")},m(a,s){L(a,l,s),ee(e,l,null),t=!0},p(a,[s]){const n={};s&7&&(n.$$scope={dirty:s,ctx:a}),e.$set(n)},i(a){t||(A(e.$$.fragment,a),t=!0)},o(a){j(e.$$.fragment,a),t=!1},d(a){a&&e&&d(l),te(e,a)}}}function ml(i,e,l){let{stats:t=null}=e,{showRevlog:a=!0}=e;return i.$$set=s=>{"stats"in s&&l(0,t=s.stats),"showRevlog"in s&&l(1,a=s.showRevlog)},[t,a]}class gl extends he{constructor(e){super(),_e(this,e,ml,_l,me,{stats:0,showRevlog:1})}}function pl(i){let e,l;return e=new gl({props:{stats:i[0].info,showRevlog:i[1]}}),{c(){Q(e.$$.fragment)},l(t){x(e.$$.fragment,t)},m(t,a){ee(e,t,a),l=!0},p(t,[a]){const s={};a&1&&(s.stats=t[0].info),e.$set(s)},i(t){l||(A(e.$$.fragment,t),l=!0)},o(t){j(e.$$.fragment,t),l=!1},d(t){te(e,t)}}}function bl(i,e,l){let t;$t(i,wt,n=>l(2,t=n));let{data:a}=e;const s=t.url.searchParams.get("revlog")!=="0";return i.$$set=n=>{"data"in n&&l(0,a=n.data)},[a,s]}class Cl extends he{constructor(e){super(),_e(this,e,bl,pl,me,{data:0})}}export{Cl as component,Vl as universal};

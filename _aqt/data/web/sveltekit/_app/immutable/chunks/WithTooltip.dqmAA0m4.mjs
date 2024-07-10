import{S as ze,i as Ve,s as qe,F as Ue,G as Ge,H as Xe,I as Ye,m as Ke,k as Qe,ae as Je}from"./Component.XCUzfIB4.mjs";import"./index.HrFqG6o2.mjs";import{g as Ze,c as St,a as $e}from"./_commonjsHelpers.1J56E-h6.mjs";import{e as tr,a as er,b as ce,c as rr,r as ir,d as nr}from"./IconButton.71V73h2j.mjs";var fe={exports:{}},M="top",I="bottom",W="right",k="left",_t="auto",ut=[M,I,W,k],rt="start",at="end",ue="clippingParents",Rt="viewport",ot="popper",pe="reference",Ct=ut.reduce(function(t,e){return t.concat([e+"-"+rt,e+"-"+at])},[]),Lt=[].concat(ut,[_t]).reduce(function(t,e){return t.concat([e,e+"-"+rt,e+"-"+at])},[]),de="beforeRead",he="read",ve="afterRead",me="beforeMain",ge="main",be="afterMain",ye="beforeWrite",_e="write",we="afterWrite",Oe=[de,he,ve,me,ge,be,ye,_e,we];function U(t){return t?(t.nodeName||"").toLowerCase():null}function z(t){if(t==null)return window;if(t.toString()!=="[object Window]"){var e=t.ownerDocument;return e&&e.defaultView||window}return t}function it(t){var e=z(t).Element;return t instanceof e||t instanceof Element}function V(t){var e=z(t).HTMLElement;return t instanceof e||t instanceof HTMLElement}function Nt(t){if(typeof ShadowRoot>"u")return!1;var e=z(t).ShadowRoot;return t instanceof e||t instanceof ShadowRoot}function or(t){var e=t.state;Object.keys(e.elements).forEach(function(r){var n=e.styles[r]||{},i=e.attributes[r]||{},o=e.elements[r];!V(o)||!U(o)||(Object.assign(o.style,n),Object.keys(i).forEach(function(c){var s=i[c];s===!1?o.removeAttribute(c):o.setAttribute(c,s===!0?"":s)}))})}function ar(t){var e=t.state,r={popper:{position:e.options.strategy,left:"0",top:"0",margin:"0"},arrow:{position:"absolute"},reference:{}};return Object.assign(e.elements.popper.style,r.popper),e.styles=r,e.elements.arrow&&Object.assign(e.elements.arrow.style,r.arrow),function(){Object.keys(e.elements).forEach(function(n){var i=e.elements[n],o=e.attributes[n]||{},c=Object.keys(e.styles.hasOwnProperty(n)?e.styles[n]:r[n]),s=c.reduce(function(a,d){return a[d]="",a},{});!V(i)||!U(i)||(Object.assign(i.style,s),Object.keys(o).forEach(function(a){i.removeAttribute(a)}))})}}const Mt={name:"applyStyles",enabled:!0,phase:"write",fn:or,effect:ar,requires:["computeStyles"]};function q(t){return t.split("-")[0]}var et=Math.max,yt=Math.min,st=Math.round;function Dt(){var t=navigator.userAgentData;return t!=null&&t.brands&&Array.isArray(t.brands)?t.brands.map(function(e){return e.brand+"/"+e.version}).join(" "):navigator.userAgent}function xe(){return!/^((?!chrome|android).)*safari/i.test(Dt())}function lt(t,e,r){e===void 0&&(e=!1),r===void 0&&(r=!1);var n=t.getBoundingClientRect(),i=1,o=1;e&&V(t)&&(i=t.offsetWidth>0&&st(n.width)/t.offsetWidth||1,o=t.offsetHeight>0&&st(n.height)/t.offsetHeight||1);var c=it(t)?z(t):window,s=c.visualViewport,a=!xe()&&r,d=(n.left+(a&&s?s.offsetLeft:0))/i,l=(n.top+(a&&s?s.offsetTop:0))/o,m=n.width/i,h=n.height/o;return{width:m,height:h,top:l,right:d+m,bottom:l+h,left:d,x:d,y:l}}function kt(t){var e=lt(t),r=t.offsetWidth,n=t.offsetHeight;return Math.abs(e.width-r)<=1&&(r=e.width),Math.abs(e.height-n)<=1&&(n=e.height),{x:t.offsetLeft,y:t.offsetTop,width:r,height:n}}function Ee(t,e){var r=e.getRootNode&&e.getRootNode();if(t.contains(e))return!0;if(r&&Nt(r)){var n=e;do{if(n&&t.isSameNode(n))return!0;n=n.parentNode||n.host}while(n)}return!1}function Z(t){return z(t).getComputedStyle(t)}function sr(t){return["table","td","th"].indexOf(U(t))>=0}function $(t){return((it(t)?t.ownerDocument:t.document)||window.document).documentElement}function wt(t){return U(t)==="html"?t:t.assignedSlot||t.parentNode||(Nt(t)?t.host:null)||$(t)}function Zt(t){return!V(t)||Z(t).position==="fixed"?null:t.offsetParent}function lr(t){var e=/firefox/i.test(Dt()),r=/Trident/i.test(Dt());if(r&&V(t)){var n=Z(t);if(n.position==="fixed")return null}var i=wt(t);for(Nt(i)&&(i=i.host);V(i)&&["html","body"].indexOf(U(i))<0;){var o=Z(i);if(o.transform!=="none"||o.perspective!=="none"||o.contain==="paint"||["transform","perspective"].indexOf(o.willChange)!==-1||e&&o.willChange==="filter"||e&&o.filter&&o.filter!=="none")return i;i=i.parentNode}return null}function ht(t){for(var e=z(t),r=Zt(t);r&&sr(r)&&Z(r).position==="static";)r=Zt(r);return r&&(U(r)==="html"||U(r)==="body"&&Z(r).position==="static")?e:r||lr(t)||e}function jt(t){return["top","bottom"].indexOf(t)>=0?"x":"y"}function pt(t,e,r){return et(t,yt(e,r))}function cr(t,e,r){var n=pt(t,e,r);return n>r?r:n}function Te(){return{top:0,right:0,bottom:0,left:0}}function Ae(t){return Object.assign({},Te(),t)}function Ce(t,e){return e.reduce(function(r,n){return r[n]=t,r},{})}var fr=function(e,r){return e=typeof e=="function"?e(Object.assign({},r.rects,{placement:r.placement})):e,Ae(typeof e!="number"?e:Ce(e,ut))};function ur(t){var e,r=t.state,n=t.name,i=t.options,o=r.elements.arrow,c=r.modifiersData.popperOffsets,s=q(r.placement),a=jt(s),d=[k,W].indexOf(s)>=0,l=d?"height":"width";if(!(!o||!c)){var m=fr(i.padding,r),h=kt(o),u=a==="y"?M:k,y=a==="y"?I:W,p=r.rects.reference[l]+r.rects.reference[a]-c[a]-r.rects.popper[l],b=c[a]-r.rects.reference[a],_=ht(o),T=_?a==="y"?_.clientHeight||0:_.clientWidth||0:0,w=p/2-b/2,g=m[u],O=T-h[l]-m[y],x=T/2-h[l]/2+w,A=pt(g,x,O),P=a;r.modifiersData[n]=(e={},e[P]=A,e.centerOffset=A-x,e)}}function pr(t){var e=t.state,r=t.options,n=r.element,i=n===void 0?"[data-popper-arrow]":n;i!=null&&(typeof i=="string"&&(i=e.elements.popper.querySelector(i),!i)||Ee(e.elements.popper,i)&&(e.elements.arrow=i))}const De={name:"arrow",enabled:!0,phase:"main",fn:ur,effect:pr,requires:["popperOffsets"],requiresIfExists:["preventOverflow"]};function ct(t){return t.split("-")[1]}var dr={top:"auto",right:"auto",bottom:"auto",left:"auto"};function hr(t,e){var r=t.x,n=t.y,i=e.devicePixelRatio||1;return{x:st(r*i)/i||0,y:st(n*i)/i||0}}function $t(t){var e,r=t.popper,n=t.popperRect,i=t.placement,o=t.variation,c=t.offsets,s=t.position,a=t.gpuAcceleration,d=t.adaptive,l=t.roundOffsets,m=t.isFixed,h=c.x,u=h===void 0?0:h,y=c.y,p=y===void 0?0:y,b=typeof l=="function"?l({x:u,y:p}):{x:u,y:p};u=b.x,p=b.y;var _=c.hasOwnProperty("x"),T=c.hasOwnProperty("y"),w=k,g=M,O=window;if(d){var x=ht(r),A="clientHeight",P="clientWidth";if(x===z(r)&&(x=$(r),Z(x).position!=="static"&&s==="absolute"&&(A="scrollHeight",P="scrollWidth")),x=x,i===M||(i===k||i===W)&&o===at){g=I;var D=m&&x===O&&O.visualViewport?O.visualViewport.height:x[A];p-=D-n.height,p*=a?1:-1}if(i===k||(i===M||i===I)&&o===at){w=W;var C=m&&x===O&&O.visualViewport?O.visualViewport.width:x[P];u-=C-n.width,u*=a?1:-1}}var S=Object.assign({position:s},d&&dr),B=l===!0?hr({x:u,y:p},z(r)):{x:u,y:p};if(u=B.x,p=B.y,a){var L;return Object.assign({},S,(L={},L[g]=T?"0":"",L[w]=_?"0":"",L.transform=(O.devicePixelRatio||1)<=1?"translate("+u+"px, "+p+"px)":"translate3d("+u+"px, "+p+"px, 0)",L))}return Object.assign({},S,(e={},e[g]=T?p+"px":"",e[w]=_?u+"px":"",e.transform="",e))}function vr(t){var e=t.state,r=t.options,n=r.gpuAcceleration,i=n===void 0?!0:n,o=r.adaptive,c=o===void 0?!0:o,s=r.roundOffsets,a=s===void 0?!0:s,d={placement:q(e.placement),variation:ct(e.placement),popper:e.elements.popper,popperRect:e.rects.popper,gpuAcceleration:i,isFixed:e.options.strategy==="fixed"};e.modifiersData.popperOffsets!=null&&(e.styles.popper=Object.assign({},e.styles.popper,$t(Object.assign({},d,{offsets:e.modifiersData.popperOffsets,position:e.options.strategy,adaptive:c,roundOffsets:a})))),e.modifiersData.arrow!=null&&(e.styles.arrow=Object.assign({},e.styles.arrow,$t(Object.assign({},d,{offsets:e.modifiersData.arrow,position:"absolute",adaptive:!1,roundOffsets:a})))),e.attributes.popper=Object.assign({},e.attributes.popper,{"data-popper-placement":e.placement})}const Bt={name:"computeStyles",enabled:!0,phase:"beforeWrite",fn:vr,data:{}};var mt={passive:!0};function mr(t){var e=t.state,r=t.instance,n=t.options,i=n.scroll,o=i===void 0?!0:i,c=n.resize,s=c===void 0?!0:c,a=z(e.elements.popper),d=[].concat(e.scrollParents.reference,e.scrollParents.popper);return o&&d.forEach(function(l){l.addEventListener("scroll",r.update,mt)}),s&&a.addEventListener("resize",r.update,mt),function(){o&&d.forEach(function(l){l.removeEventListener("scroll",r.update,mt)}),s&&a.removeEventListener("resize",r.update,mt)}}const Ft={name:"eventListeners",enabled:!0,phase:"write",fn:function(){},effect:mr,data:{}};var gr={left:"right",right:"left",bottom:"top",top:"bottom"};function bt(t){return t.replace(/left|right|bottom|top/g,function(e){return gr[e]})}var br={start:"end",end:"start"};function te(t){return t.replace(/start|end/g,function(e){return br[e]})}function Ht(t){var e=z(t),r=e.pageXOffset,n=e.pageYOffset;return{scrollLeft:r,scrollTop:n}}function It(t){return lt($(t)).left+Ht(t).scrollLeft}function yr(t,e){var r=z(t),n=$(t),i=r.visualViewport,o=n.clientWidth,c=n.clientHeight,s=0,a=0;if(i){o=i.width,c=i.height;var d=xe();(d||!d&&e==="fixed")&&(s=i.offsetLeft,a=i.offsetTop)}return{width:o,height:c,x:s+It(t),y:a}}function _r(t){var e,r=$(t),n=Ht(t),i=(e=t.ownerDocument)==null?void 0:e.body,o=et(r.scrollWidth,r.clientWidth,i?i.scrollWidth:0,i?i.clientWidth:0),c=et(r.scrollHeight,r.clientHeight,i?i.scrollHeight:0,i?i.clientHeight:0),s=-n.scrollLeft+It(t),a=-n.scrollTop;return Z(i||r).direction==="rtl"&&(s+=et(r.clientWidth,i?i.clientWidth:0)-o),{width:o,height:c,x:s,y:a}}function Wt(t){var e=Z(t),r=e.overflow,n=e.overflowX,i=e.overflowY;return/auto|scroll|overlay|hidden/.test(r+i+n)}function Pe(t){return["html","body","#document"].indexOf(U(t))>=0?t.ownerDocument.body:V(t)&&Wt(t)?t:Pe(wt(t))}function dt(t,e){var r;e===void 0&&(e=[]);var n=Pe(t),i=n===((r=t.ownerDocument)==null?void 0:r.body),o=z(n),c=i?[o].concat(o.visualViewport||[],Wt(n)?n:[]):n,s=e.concat(c);return i?s:s.concat(dt(wt(c)))}function Pt(t){return Object.assign({},t,{left:t.x,top:t.y,right:t.x+t.width,bottom:t.y+t.height})}function wr(t,e){var r=lt(t,!1,e==="fixed");return r.top=r.top+t.clientTop,r.left=r.left+t.clientLeft,r.bottom=r.top+t.clientHeight,r.right=r.left+t.clientWidth,r.width=t.clientWidth,r.height=t.clientHeight,r.x=r.left,r.y=r.top,r}function ee(t,e,r){return e===Rt?Pt(yr(t,r)):it(e)?wr(e,r):Pt(_r($(t)))}function Or(t){var e=dt(wt(t)),r=["absolute","fixed"].indexOf(Z(t).position)>=0,n=r&&V(t)?ht(t):t;return it(n)?e.filter(function(i){return it(i)&&Ee(i,n)&&U(i)!=="body"}):[]}function xr(t,e,r,n){var i=e==="clippingParents"?Or(t):[].concat(e),o=[].concat(i,[r]),c=o[0],s=o.reduce(function(a,d){var l=ee(t,d,n);return a.top=et(l.top,a.top),a.right=yt(l.right,a.right),a.bottom=yt(l.bottom,a.bottom),a.left=et(l.left,a.left),a},ee(t,c,n));return s.width=s.right-s.left,s.height=s.bottom-s.top,s.x=s.left,s.y=s.top,s}function Se(t){var e=t.reference,r=t.element,n=t.placement,i=n?q(n):null,o=n?ct(n):null,c=e.x+e.width/2-r.width/2,s=e.y+e.height/2-r.height/2,a;switch(i){case M:a={x:c,y:e.y-r.height};break;case I:a={x:c,y:e.y+e.height};break;case W:a={x:e.x+e.width,y:s};break;case k:a={x:e.x-r.width,y:s};break;default:a={x:e.x,y:e.y}}var d=i?jt(i):null;if(d!=null){var l=d==="y"?"height":"width";switch(o){case rt:a[d]=a[d]-(e[l]/2-r[l]/2);break;case at:a[d]=a[d]+(e[l]/2-r[l]/2);break}}return a}function ft(t,e){e===void 0&&(e={});var r=e,n=r.placement,i=n===void 0?t.placement:n,o=r.strategy,c=o===void 0?t.strategy:o,s=r.boundary,a=s===void 0?ue:s,d=r.rootBoundary,l=d===void 0?Rt:d,m=r.elementContext,h=m===void 0?ot:m,u=r.altBoundary,y=u===void 0?!1:u,p=r.padding,b=p===void 0?0:p,_=Ae(typeof b!="number"?b:Ce(b,ut)),T=h===ot?pe:ot,w=t.rects.popper,g=t.elements[y?T:h],O=xr(it(g)?g:g.contextElement||$(t.elements.popper),a,l,c),x=lt(t.elements.reference),A=Se({reference:x,element:w,strategy:"absolute",placement:i}),P=Pt(Object.assign({},w,A)),D=h===ot?P:x,C={top:O.top-D.top+_.top,bottom:D.bottom-O.bottom+_.bottom,left:O.left-D.left+_.left,right:D.right-O.right+_.right},S=t.modifiersData.offset;if(h===ot&&S){var B=S[i];Object.keys(C).forEach(function(L){var G=[W,I].indexOf(L)>=0?1:-1,X=[M,I].indexOf(L)>=0?"y":"x";C[L]+=B[X]*G})}return C}function Er(t,e){e===void 0&&(e={});var r=e,n=r.placement,i=r.boundary,o=r.rootBoundary,c=r.padding,s=r.flipVariations,a=r.allowedAutoPlacements,d=a===void 0?Lt:a,l=ct(n),m=l?s?Ct:Ct.filter(function(y){return ct(y)===l}):ut,h=m.filter(function(y){return d.indexOf(y)>=0});h.length===0&&(h=m);var u=h.reduce(function(y,p){return y[p]=ft(t,{placement:p,boundary:i,rootBoundary:o,padding:c})[q(p)],y},{});return Object.keys(u).sort(function(y,p){return u[y]-u[p]})}function Tr(t){if(q(t)===_t)return[];var e=bt(t);return[te(t),e,te(e)]}function Ar(t){var e=t.state,r=t.options,n=t.name;if(!e.modifiersData[n]._skip){for(var i=r.mainAxis,o=i===void 0?!0:i,c=r.altAxis,s=c===void 0?!0:c,a=r.fallbackPlacements,d=r.padding,l=r.boundary,m=r.rootBoundary,h=r.altBoundary,u=r.flipVariations,y=u===void 0?!0:u,p=r.allowedAutoPlacements,b=e.options.placement,_=q(b),T=_===b,w=a||(T||!y?[bt(b)]:Tr(b)),g=[b].concat(w).reduce(function(E,R){return E.concat(q(R)===_t?Er(e,{placement:R,boundary:l,rootBoundary:m,padding:d,flipVariations:y,allowedAutoPlacements:p}):R)},[]),O=e.rects.reference,x=e.rects.popper,A=new Map,P=!0,D=g[0],C=0;C<g.length;C++){var S=g[C],B=q(S),L=ct(S)===rt,G=[M,I].indexOf(B)>=0,X=G?"width":"height",N=ft(e,{placement:S,boundary:l,rootBoundary:m,altBoundary:h,padding:d}),F=G?L?W:k:L?I:M;O[X]>x[X]&&(F=bt(F));var nt=bt(F),Y=[];if(o&&Y.push(N[B]<=0),s&&Y.push(N[F]<=0,N[nt]<=0),Y.every(function(E){return E})){D=S,P=!1;break}A.set(S,Y)}if(P)for(var K=y?3:1,Q=function(R){var j=g.find(function(H){var J=A.get(H);if(J)return J.slice(0,R).every(function(xt){return xt})});if(j)return D=j,"break"},f=K;f>0;f--){var v=Q(f);if(v==="break")break}e.placement!==D&&(e.modifiersData[n]._skip=!0,e.placement=D,e.reset=!0)}}const Re={name:"flip",enabled:!0,phase:"main",fn:Ar,requiresIfExists:["offset"],data:{_skip:!1}};function re(t,e,r){return r===void 0&&(r={x:0,y:0}),{top:t.top-e.height-r.y,right:t.right-e.width+r.x,bottom:t.bottom-e.height+r.y,left:t.left-e.width-r.x}}function ie(t){return[M,W,I,k].some(function(e){return t[e]>=0})}function Cr(t){var e=t.state,r=t.name,n=e.rects.reference,i=e.rects.popper,o=e.modifiersData.preventOverflow,c=ft(e,{elementContext:"reference"}),s=ft(e,{altBoundary:!0}),a=re(c,n),d=re(s,i,o),l=ie(a),m=ie(d);e.modifiersData[r]={referenceClippingOffsets:a,popperEscapeOffsets:d,isReferenceHidden:l,hasPopperEscaped:m},e.attributes.popper=Object.assign({},e.attributes.popper,{"data-popper-reference-hidden":l,"data-popper-escaped":m})}const Le={name:"hide",enabled:!0,phase:"main",requiresIfExists:["preventOverflow"],fn:Cr};function Dr(t,e,r){var n=q(t),i=[k,M].indexOf(n)>=0?-1:1,o=typeof r=="function"?r(Object.assign({},e,{placement:t})):r,c=o[0],s=o[1];return c=c||0,s=(s||0)*i,[k,W].indexOf(n)>=0?{x:s,y:c}:{x:c,y:s}}function Pr(t){var e=t.state,r=t.options,n=t.name,i=r.offset,o=i===void 0?[0,0]:i,c=Lt.reduce(function(l,m){return l[m]=Dr(m,e.rects,o),l},{}),s=c[e.placement],a=s.x,d=s.y;e.modifiersData.popperOffsets!=null&&(e.modifiersData.popperOffsets.x+=a,e.modifiersData.popperOffsets.y+=d),e.modifiersData[n]=c}const Ne={name:"offset",enabled:!0,phase:"main",requires:["popperOffsets"],fn:Pr};function Sr(t){var e=t.state,r=t.name;e.modifiersData[r]=Se({reference:e.rects.reference,element:e.rects.popper,strategy:"absolute",placement:e.placement})}const zt={name:"popperOffsets",enabled:!0,phase:"read",fn:Sr,data:{}};function Rr(t){return t==="x"?"y":"x"}function Lr(t){var e=t.state,r=t.options,n=t.name,i=r.mainAxis,o=i===void 0?!0:i,c=r.altAxis,s=c===void 0?!1:c,a=r.boundary,d=r.rootBoundary,l=r.altBoundary,m=r.padding,h=r.tether,u=h===void 0?!0:h,y=r.tetherOffset,p=y===void 0?0:y,b=ft(e,{boundary:a,rootBoundary:d,padding:m,altBoundary:l}),_=q(e.placement),T=ct(e.placement),w=!T,g=jt(_),O=Rr(g),x=e.modifiersData.popperOffsets,A=e.rects.reference,P=e.rects.popper,D=typeof p=="function"?p(Object.assign({},e.rects,{placement:e.placement})):p,C=typeof D=="number"?{mainAxis:D,altAxis:D}:Object.assign({mainAxis:0,altAxis:0},D),S=e.modifiersData.offset?e.modifiersData.offset[e.placement]:null,B={x:0,y:0};if(x){if(o){var L,G=g==="y"?M:k,X=g==="y"?I:W,N=g==="y"?"height":"width",F=x[g],nt=F+b[G],Y=F-b[X],K=u?-P[N]/2:0,Q=T===rt?A[N]:P[N],f=T===rt?-P[N]:-A[N],v=e.elements.arrow,E=u&&v?kt(v):{width:0,height:0},R=e.modifiersData["arrow#persistent"]?e.modifiersData["arrow#persistent"].padding:Te(),j=R[G],H=R[X],J=pt(0,A[N],E[N]),xt=w?A[N]/2-K-J-j-C.mainAxis:Q-J-j-C.mainAxis,je=w?-A[N]/2+K+J+H+C.mainAxis:f+J+H+C.mainAxis,Et=e.elements.arrow&&ht(e.elements.arrow),Be=Et?g==="y"?Et.clientTop||0:Et.clientLeft||0:0,Vt=(L=S==null?void 0:S[g])!=null?L:0,Fe=F+xt-Vt-Be,He=F+je-Vt,qt=pt(u?yt(nt,Fe):nt,F,u?et(Y,He):Y);x[g]=qt,B[g]=qt-F}if(s){var Ut,Ie=g==="x"?M:k,We=g==="x"?I:W,tt=x[O],vt=O==="y"?"height":"width",Gt=tt+b[Ie],Xt=tt-b[We],Tt=[M,k].indexOf(_)!==-1,Yt=(Ut=S==null?void 0:S[O])!=null?Ut:0,Kt=Tt?Gt:tt-A[vt]-P[vt]-Yt+C.altAxis,Qt=Tt?tt+A[vt]+P[vt]-Yt-C.altAxis:Xt,Jt=u&&Tt?cr(Kt,tt,Qt):pt(u?Kt:Gt,tt,u?Qt:Xt);x[O]=Jt,B[O]=Jt-tt}e.modifiersData[n]=B}}const Me={name:"preventOverflow",enabled:!0,phase:"main",fn:Lr,requiresIfExists:["offset"]};function Nr(t){return{scrollLeft:t.scrollLeft,scrollTop:t.scrollTop}}function Mr(t){return t===z(t)||!V(t)?Ht(t):Nr(t)}function kr(t){var e=t.getBoundingClientRect(),r=st(e.width)/t.offsetWidth||1,n=st(e.height)/t.offsetHeight||1;return r!==1||n!==1}function jr(t,e,r){r===void 0&&(r=!1);var n=V(e),i=V(e)&&kr(e),o=$(e),c=lt(t,i,r),s={scrollLeft:0,scrollTop:0},a={x:0,y:0};return(n||!n&&!r)&&((U(e)!=="body"||Wt(o))&&(s=Mr(e)),V(e)?(a=lt(e,!0),a.x+=e.clientLeft,a.y+=e.clientTop):o&&(a.x=It(o))),{x:c.left+s.scrollLeft-a.x,y:c.top+s.scrollTop-a.y,width:c.width,height:c.height}}function Br(t){var e=new Map,r=new Set,n=[];t.forEach(function(o){e.set(o.name,o)});function i(o){r.add(o.name);var c=[].concat(o.requires||[],o.requiresIfExists||[]);c.forEach(function(s){if(!r.has(s)){var a=e.get(s);a&&i(a)}}),n.push(o)}return t.forEach(function(o){r.has(o.name)||i(o)}),n}function Fr(t){var e=Br(t);return Oe.reduce(function(r,n){return r.concat(e.filter(function(i){return i.phase===n}))},[])}function Hr(t){var e;return function(){return e||(e=new Promise(function(r){Promise.resolve().then(function(){e=void 0,r(t())})})),e}}function Ir(t){var e=t.reduce(function(r,n){var i=r[n.name];return r[n.name]=i?Object.assign({},i,n,{options:Object.assign({},i.options,n.options),data:Object.assign({},i.data,n.data)}):n,r},{});return Object.keys(e).map(function(r){return e[r]})}var ne={placement:"bottom",modifiers:[],strategy:"absolute"};function oe(){for(var t=arguments.length,e=new Array(t),r=0;r<t;r++)e[r]=arguments[r];return!e.some(function(n){return!(n&&typeof n.getBoundingClientRect=="function")})}function Ot(t){t===void 0&&(t={});var e=t,r=e.defaultModifiers,n=r===void 0?[]:r,i=e.defaultOptions,o=i===void 0?ne:i;return function(s,a,d){d===void 0&&(d=o);var l={placement:"bottom",orderedModifiers:[],options:Object.assign({},ne,o),modifiersData:{},elements:{reference:s,popper:a},attributes:{},styles:{}},m=[],h=!1,u={state:l,setOptions:function(_){var T=typeof _=="function"?_(l.options):_;p(),l.options=Object.assign({},o,l.options,T),l.scrollParents={reference:it(s)?dt(s):s.contextElement?dt(s.contextElement):[],popper:dt(a)};var w=Fr(Ir([].concat(n,l.options.modifiers)));return l.orderedModifiers=w.filter(function(g){return g.enabled}),y(),u.update()},forceUpdate:function(){if(!h){var _=l.elements,T=_.reference,w=_.popper;if(oe(T,w)){l.rects={reference:jr(T,ht(w),l.options.strategy==="fixed"),popper:kt(w)},l.reset=!1,l.placement=l.options.placement,l.orderedModifiers.forEach(function(C){return l.modifiersData[C.name]=Object.assign({},C.data)});for(var g=0;g<l.orderedModifiers.length;g++){if(l.reset===!0){l.reset=!1,g=-1;continue}var O=l.orderedModifiers[g],x=O.fn,A=O.options,P=A===void 0?{}:A,D=O.name;typeof x=="function"&&(l=x({state:l,options:P,name:D,instance:u})||l)}}}},update:Hr(function(){return new Promise(function(b){u.forceUpdate(),b(l)})}),destroy:function(){p(),h=!0}};if(!oe(s,a))return u;u.setOptions(d).then(function(b){!h&&d.onFirstUpdate&&d.onFirstUpdate(b)});function y(){l.orderedModifiers.forEach(function(b){var _=b.name,T=b.options,w=T===void 0?{}:T,g=b.effect;if(typeof g=="function"){var O=g({state:l,name:_,instance:u,options:w}),x=function(){};m.push(O||x)}})}function p(){m.forEach(function(b){return b()}),m=[]}return u}}var Wr=Ot(),zr=[Ft,zt,Bt,Mt],Vr=Ot({defaultModifiers:zr}),qr=[Ft,zt,Bt,Mt,Ne,Re,Me,De,Le],Ur=Ot({defaultModifiers:qr});const Gr=Object.freeze(Object.defineProperty({__proto__:null,afterMain:be,afterRead:ve,afterWrite:we,applyStyles:Mt,arrow:De,auto:_t,basePlacements:ut,beforeMain:me,beforeRead:de,beforeWrite:ye,bottom:I,clippingParents:ue,computeStyles:Bt,createPopper:Ur,createPopperBase:Wr,createPopperLite:Vr,detectOverflow:ft,end:at,eventListeners:Ft,flip:Re,hide:Le,left:k,main:ge,modifierPhases:Oe,offset:Ne,placements:Lt,popper:ot,popperGenerator:Ot,popperOffsets:zt,preventOverflow:Me,read:he,reference:pe,right:W,start:rt,top:M,variationPlacements:Ct,viewport:Rt,write:_e},Symbol.toStringTag,{value:"Module"})),Xr=Ze(Gr);var gt={exports:{}};/*!
  * Bootstrap sanitizer.js v5.3.3 (https://getbootstrap.com/)
  * Copyright 2011-2024 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
  */var ae;function ke(){return ae||(ae=1,function(t,e){(function(r,n){n(e)})(St,function(r){const i={"*":["class","dir","id","lang","role",/^aria-[\w-]*$/i],a:["target","href","title","rel"],area:[],b:[],br:[],col:[],code:[],dd:[],div:[],dl:[],dt:[],em:[],hr:[],h1:[],h2:[],h3:[],h4:[],h5:[],h6:[],i:[],img:["src","srcset","alt","title","width","height"],li:[],ol:[],p:[],pre:[],s:[],small:[],span:[],sub:[],sup:[],strong:[],u:[],ul:[]},o=new Set(["background","cite","href","itemtype","longdesc","poster","src","xlink:href"]),c=/^(?!javascript:)(?:[a-z0-9+.-]+:|[^&:/?#]*(?:[/?#]|$))/i,s=(d,l)=>{const m=d.nodeName.toLowerCase();return l.includes(m)?o.has(m)?!!c.test(d.nodeValue):!0:l.filter(h=>h instanceof RegExp).some(h=>h.test(m))};function a(d,l,m){if(!d.length)return d;if(m&&typeof m=="function")return m(d);const u=new window.DOMParser().parseFromString(d,"text/html"),y=[].concat(...u.body.querySelectorAll("*"));for(const p of y){const b=p.nodeName.toLowerCase();if(!Object.keys(l).includes(b)){p.remove();continue}const _=[].concat(...p.attributes),T=[].concat(l["*"]||[],l[b]||[]);for(const w of _)s(w,T)||p.removeAttribute(w.nodeName)}return u.body.innerHTML}r.DefaultAllowlist=i,r.sanitizeHtml=a,Object.defineProperty(r,Symbol.toStringTag,{value:"Module"})})}(gt,gt.exports)),gt.exports}var At={exports:{}};/*!
  * Bootstrap template-factory.js v5.3.3 (https://getbootstrap.com/)
  * Copyright 2011-2024 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
  */var se;function Yr(){return se||(se=1,function(t,e){(function(r,n){t.exports=n(tr(),er(),ke(),ce())})(St,function(r,n,i,o){const c="TemplateFactory",s={allowList:i.DefaultAllowlist,content:{},extraClass:"",html:!1,sanitize:!0,sanitizeFn:null,template:"<div></div>"},a={allowList:"object",content:"object",extraClass:"(string|function)",html:"boolean",sanitize:"boolean",sanitizeFn:"(null|function)",template:"string"},d={entry:"(string|element|function|null)",selector:"(string|element)"};class l extends n{constructor(h){super(),this._config=this._getConfig(h)}static get Default(){return s}static get DefaultType(){return a}static get NAME(){return c}getContent(){return Object.values(this._config.content).map(h=>this._resolvePossibleFunction(h)).filter(Boolean)}hasContent(){return this.getContent().length>0}changeContent(h){return this._checkContent(h),this._config.content={...this._config.content,...h},this}toHtml(){const h=document.createElement("div");h.innerHTML=this._maybeSanitize(this._config.template);for(const[p,b]of Object.entries(this._config.content))this._setContent(h,b,p);const u=h.children[0],y=this._resolvePossibleFunction(this._config.extraClass);return y&&u.classList.add(...y.split(" ")),u}_typeCheckConfig(h){super._typeCheckConfig(h),this._checkContent(h.content)}_checkContent(h){for(const[u,y]of Object.entries(h))super._typeCheckConfig({selector:u,entry:y},d)}_setContent(h,u,y){const p=r.findOne(y,h);if(p){if(u=this._resolvePossibleFunction(u),!u){p.remove();return}if(o.isElement(u)){this._putElementInTemplate(o.getElement(u),p);return}if(this._config.html){p.innerHTML=this._maybeSanitize(u);return}p.textContent=u}}_maybeSanitize(h){return this._config.sanitize?i.sanitizeHtml(h,this._config.allowList,this._config.sanitizeFn):h}_resolvePossibleFunction(h){return o.execute(h,[this])}_putElementInTemplate(h,u){if(this._config.html){u.innerHTML="",u.append(h);return}u.textContent=h.textContent}}return l})}(At)),At.exports}/*!
  * Bootstrap tooltip.js v5.3.3 (https://getbootstrap.com/)
  * Copyright 2011-2024 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
  */(function(t,e){(function(r,n){t.exports=n(Xr,rr(),ir(),nr(),ce(),ke(),Yr())})(St,function(r,n,i,o,c,s,a){function d(Q){const f=Object.create(null,{[Symbol.toStringTag]:{value:"Module"}});if(Q){for(const v in Q)if(v!=="default"){const E=Object.getOwnPropertyDescriptor(Q,v);Object.defineProperty(f,v,E.get?E:{enumerable:!0,get:()=>Q[v]})}}return f.default=Q,Object.freeze(f)}const l=d(r),m="tooltip",h=new Set(["sanitize","allowList","sanitizeFn"]),u="fade",y="modal",p="show",b=".tooltip-inner",_=`.${y}`,T="hide.bs.modal",w="hover",g="focus",O="click",x="manual",A="hide",P="hidden",D="show",C="shown",S="inserted",B="click",L="focusin",G="focusout",X="mouseenter",N="mouseleave",F={AUTO:"auto",TOP:"top",RIGHT:c.isRTL()?"left":"right",BOTTOM:"bottom",LEFT:c.isRTL()?"right":"left"},nt={allowList:s.DefaultAllowlist,animation:!0,boundary:"clippingParents",container:!1,customClass:"",delay:0,fallbackPlacements:["top","right","bottom","left"],html:!1,offset:[0,6],placement:"top",popperConfig:null,sanitize:!0,sanitizeFn:null,selector:!1,template:'<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',title:"",trigger:"hover focus"},Y={allowList:"object",animation:"boolean",boundary:"(string|element)",container:"(string|element|boolean)",customClass:"(string|function)",delay:"(number|object)",fallbackPlacements:"array",html:"boolean",offset:"(array|string|function)",placement:"(string|function)",popperConfig:"(null|object|function)",sanitize:"boolean",sanitizeFn:"(null|function)",selector:"(string|boolean)",template:"string",title:"(string|element|function)",trigger:"string"};class K extends n{constructor(f,v){if(typeof l>"u")throw new TypeError("Bootstrap's tooltips require Popper (https://popper.js.org)");super(f,v),this._isEnabled=!0,this._timeout=0,this._isHovered=null,this._activeTrigger={},this._popper=null,this._templateFactory=null,this._newContent=null,this.tip=null,this._setListeners(),this._config.selector||this._fixTitle()}static get Default(){return nt}static get DefaultType(){return Y}static get NAME(){return m}enable(){this._isEnabled=!0}disable(){this._isEnabled=!1}toggleEnabled(){this._isEnabled=!this._isEnabled}toggle(){if(this._isEnabled){if(this._activeTrigger.click=!this._activeTrigger.click,this._isShown()){this._leave();return}this._enter()}}dispose(){clearTimeout(this._timeout),i.off(this._element.closest(_),T,this._hideModalHandler),this._element.getAttribute("data-bs-original-title")&&this._element.setAttribute("title",this._element.getAttribute("data-bs-original-title")),this._disposePopper(),super.dispose()}show(){if(this._element.style.display==="none")throw new Error("Please use show on visible elements");if(!(this._isWithContent()&&this._isEnabled))return;const f=i.trigger(this._element,this.constructor.eventName(D)),E=(c.findShadowRoot(this._element)||this._element.ownerDocument.documentElement).contains(this._element);if(f.defaultPrevented||!E)return;this._disposePopper();const R=this._getTipElement();this._element.setAttribute("aria-describedby",R.getAttribute("id"));const{container:j}=this._config;if(this._element.ownerDocument.documentElement.contains(this.tip)||(j.append(R),i.trigger(this._element,this.constructor.eventName(S))),this._popper=this._createPopper(R),R.classList.add(p),"ontouchstart"in document.documentElement)for(const J of[].concat(...document.body.children))i.on(J,"mouseover",c.noop);const H=()=>{i.trigger(this._element,this.constructor.eventName(C)),this._isHovered===!1&&this._leave(),this._isHovered=!1};this._queueCallback(H,this.tip,this._isAnimated())}hide(){if(!this._isShown()||i.trigger(this._element,this.constructor.eventName(A)).defaultPrevented)return;if(this._getTipElement().classList.remove(p),"ontouchstart"in document.documentElement)for(const R of[].concat(...document.body.children))i.off(R,"mouseover",c.noop);this._activeTrigger[O]=!1,this._activeTrigger[g]=!1,this._activeTrigger[w]=!1,this._isHovered=null;const E=()=>{this._isWithActiveTrigger()||(this._isHovered||this._disposePopper(),this._element.removeAttribute("aria-describedby"),i.trigger(this._element,this.constructor.eventName(P)))};this._queueCallback(E,this.tip,this._isAnimated())}update(){this._popper&&this._popper.update()}_isWithContent(){return!!this._getTitle()}_getTipElement(){return this.tip||(this.tip=this._createTipElement(this._newContent||this._getContentForTemplate())),this.tip}_createTipElement(f){const v=this._getTemplateFactory(f).toHtml();if(!v)return null;v.classList.remove(u,p),v.classList.add(`bs-${this.constructor.NAME}-auto`);const E=c.getUID(this.constructor.NAME).toString();return v.setAttribute("id",E),this._isAnimated()&&v.classList.add(u),v}setContent(f){this._newContent=f,this._isShown()&&(this._disposePopper(),this.show())}_getTemplateFactory(f){return this._templateFactory?this._templateFactory.changeContent(f):this._templateFactory=new a({...this._config,content:f,extraClass:this._resolvePossibleFunction(this._config.customClass)}),this._templateFactory}_getContentForTemplate(){return{[b]:this._getTitle()}}_getTitle(){return this._resolvePossibleFunction(this._config.title)||this._element.getAttribute("data-bs-original-title")}_initializeOnDelegatedTarget(f){return this.constructor.getOrCreateInstance(f.delegateTarget,this._getDelegateConfig())}_isAnimated(){return this._config.animation||this.tip&&this.tip.classList.contains(u)}_isShown(){return this.tip&&this.tip.classList.contains(p)}_createPopper(f){const v=c.execute(this._config.placement,[this,f,this._element]),E=F[v.toUpperCase()];return l.createPopper(this._element,f,this._getPopperConfig(E))}_getOffset(){const{offset:f}=this._config;return typeof f=="string"?f.split(",").map(v=>Number.parseInt(v,10)):typeof f=="function"?v=>f(v,this._element):f}_resolvePossibleFunction(f){return c.execute(f,[this._element])}_getPopperConfig(f){const v={placement:f,modifiers:[{name:"flip",options:{fallbackPlacements:this._config.fallbackPlacements}},{name:"offset",options:{offset:this._getOffset()}},{name:"preventOverflow",options:{boundary:this._config.boundary}},{name:"arrow",options:{element:`.${this.constructor.NAME}-arrow`}},{name:"preSetPlacement",enabled:!0,phase:"beforeMain",fn:E=>{this._getTipElement().setAttribute("data-popper-placement",E.state.placement)}}]};return{...v,...c.execute(this._config.popperConfig,[v])}}_setListeners(){const f=this._config.trigger.split(" ");for(const v of f)if(v==="click")i.on(this._element,this.constructor.eventName(B),this._config.selector,E=>{this._initializeOnDelegatedTarget(E).toggle()});else if(v!==x){const E=v===w?this.constructor.eventName(X):this.constructor.eventName(L),R=v===w?this.constructor.eventName(N):this.constructor.eventName(G);i.on(this._element,E,this._config.selector,j=>{const H=this._initializeOnDelegatedTarget(j);H._activeTrigger[j.type==="focusin"?g:w]=!0,H._enter()}),i.on(this._element,R,this._config.selector,j=>{const H=this._initializeOnDelegatedTarget(j);H._activeTrigger[j.type==="focusout"?g:w]=H._element.contains(j.relatedTarget),H._leave()})}this._hideModalHandler=()=>{this._element&&this.hide()},i.on(this._element.closest(_),T,this._hideModalHandler)}_fixTitle(){const f=this._element.getAttribute("title");f&&(!this._element.getAttribute("aria-label")&&!this._element.textContent.trim()&&this._element.setAttribute("aria-label",f),this._element.setAttribute("data-bs-original-title",f),this._element.removeAttribute("title"))}_enter(){if(this._isShown()||this._isHovered){this._isHovered=!0;return}this._isHovered=!0,this._setTimeout(()=>{this._isHovered&&this.show()},this._config.delay.show)}_leave(){this._isWithActiveTrigger()||(this._isHovered=!1,this._setTimeout(()=>{this._isHovered||this.hide()},this._config.delay.hide))}_setTimeout(f,v){clearTimeout(this._timeout),this._timeout=setTimeout(f,v)}_isWithActiveTrigger(){return Object.values(this._activeTrigger).includes(!0)}_getConfig(f){const v=o.getDataAttributes(this._element);for(const E of Object.keys(v))h.has(E)&&delete v[E];return f={...v,...typeof f=="object"&&f?f:{}},f=this._mergeConfigObj(f),f=this._configAfterMerge(f),this._typeCheckConfig(f),f}_configAfterMerge(f){return f.container=f.container===!1?document.body:c.getElement(f.container),typeof f.delay=="number"&&(f.delay={show:f.delay,hide:f.delay}),typeof f.title=="number"&&(f.title=f.title.toString()),typeof f.content=="number"&&(f.content=f.content.toString()),f}_getDelegateConfig(){const f={};for(const[v,E]of Object.entries(this._config))this.constructor.Default[v]!==E&&(f[v]=E);return f.selector=!1,f.trigger="manual",f}_disposePopper(){this._popper&&(this._popper.destroy(),this._popper=null),this.tip&&(this.tip.remove(),this.tip=null)}static jQueryInterface(f){return this.each(function(){const v=K.getOrCreateInstance(this,f);if(typeof f=="string"){if(typeof v[f]>"u")throw new TypeError(`No method named "${f}"`);v[f]()}})}}return c.defineJQueryPlugin(K),K})})(fe);var Kr=fe.exports;const Qr=$e(Kr),Jr=t=>({tooltipObject:t&1}),le=t=>({createTooltip:t[1],tooltipObject:t[0]});function Zr(t){let e;const r=t[10].default,n=Ue(r,t,t[9],le);return{c(){n&&n.c()},l(i){n&&n.l(i)},m(i,o){n&&n.m(i,o),e=!0},p(i,[o]){n&&n.p&&(!e||o&513)&&Ge(n,r,i,i[9],e?Ye(r,i[9],o,Jr):Xe(i[9]),le)},i(i){e||(Ke(n,i),e=!0)},o(i){Qe(n,i),e=!1},d(i){n&&n.d(i)}}}function $r(t,e,r){let{$$slots:n={},$$scope:i}=e,{tooltip:o}=e,{trigger:c="hover focus"}=e,{placement:s="top"}=e,{html:a=!0}=e,{offset:d=[0,0]}=e,{showDelay:l=0}=e,{hideDelay:m=0}=e,h,u;function y(p){h=p,p.title=o,r(0,u=new Qr(p,{placement:s,html:a,offset:d,delay:{show:l,hide:m},trigger:c}))}return Je(()=>{h==null||h.addEventListener("hidden.bs.tooltip",()=>{u==null||u.dispose()}),u==null||u.hide()}),t.$$set=p=>{"tooltip"in p&&r(2,o=p.tooltip),"trigger"in p&&r(3,c=p.trigger),"placement"in p&&r(4,s=p.placement),"html"in p&&r(5,a=p.html),"offset"in p&&r(6,d=p.offset),"showDelay"in p&&r(7,l=p.showDelay),"hideDelay"in p&&r(8,m=p.hideDelay),"$$scope"in p&&r(9,i=p.$$scope)},[u,y,o,c,s,a,d,l,m,i,n]}class ni extends ze{constructor(e){super(),Ve(this,e,$r,Zr,qe,{tooltip:2,trigger:3,placement:4,html:5,offset:6,showDelay:7,hideDelay:8})}}export{ni as W};

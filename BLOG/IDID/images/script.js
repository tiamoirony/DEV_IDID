;(function($) {
    /**
     * nOo9ya skin config
     */
    var role = window.T.config.ROLE;
    $.config = {
        logo : function(logo, title, img) {
            logo = logo !== undefined ? logo : false;
            title = title !== undefined ? title : ".blog-logo .title";
            img = img !== undefined ? img : ".blog-logo .img-profile";

            if (logo === true) {
                $(img).show();
                $(title).hide();
            } else {
                $(img).hide();
                $(title).show();
            }
        },

        adminLink : function(target, check) {
            target = target !== undefined ? target : "#footerAdmin";
            check = check !== undefined ? check : true;

            if (check === true) {
                role == "owner" ? $(target).show() : $(target).hide();
            }
        }
    };

    /**
     * skin variable
     * #1 Tistory Theme 참조
     */
    var Area = {};

    Area.SocialShare = (function() {
        var SOCIAL_SHARE = {
            kakaostory: {
                url: "https://story.kakao.com/share",
                width: 640,
                height: 400,
                makeShareUrl: function(url) {
                    return this.url + "?url=" + encodeURIComponent(url);
                }
            },
            facebook: {
                url: "https://www.facebook.com/sharer/sharer.php",
                width: 640,
                height: 400,
                makeShareUrl: function(url) {
                    return this.url + "?display=popup&u=" + encodeURIComponent(url);
                }
            },
            twitter: {
                url: "https://twitter.com/intent/tweet",
                width: 640,
                height: 400,
                makeShareUrl: function(url) {
                    return this.url + "?url=" + encodeURIComponent(url);
                }
            }
        };

        var onClick = function(e) {
            var $this = $(this),
                service = SOCIAL_SHARE[$this.data("service")],
                url = location.href;

            if (service) {
                e.preventDefault();
                window.open(service.makeShareUrl(url), "", "width=" + service.width + ", height=" + service.height);
            }
        };

        var init = function() {

        };

        $(".article-share").on("click", "a", onClick);

        return {
            init: init
        }
    })();

    Area.init = function() {
        Area.SocialShare.init();
    };

    $.Area = Area;

    var $allVideos = $("iframe[src^='//player.vimeo.com'], iframe[src^='//www.youtube.com'], object, embed, iframe[src^='http://www.youtube.com'], iframe[src^='https://www.youtube.com'], iframe[src^='http://videofarm.daum.net'], iframe[src^='https://videofarm.daum.net'], iframe[src^='//videofarm.daum.net'], iframe[src^='//tv.kakao.com'], iframe[src^='//kakaotv.daum.net']"),
        $fluidEl = $(".article");

    $allVideos.each(function() {
        $(this)
            // jQuery .data does not work on object/embed elements
            .attr('data-aspectRatio', this.height / this.width)
            .removeAttr('height')
            .removeAttr('width');
    });

    $(window).resize(function() {

        var newWidth = $fluidEl.width();
        $allVideos.each(function() {
            var $el = $(this);
            $el
                .width(newWidth)
                .height(newWidth * $el.attr('data-aspectRatio'));
        });

    }).resize();

})(jQuery);

/***************************
    CODE BLOCK
****************************/

const COPY_TEXT_CHANGE_OFFSET = 1000;
const COPY_BUTTON_TEXT_BEFORE = 'Copy';
const COPY_BUTTON_TEXT_AFTER = 'Copied';
const COPY_ERROR_MESSAGE = '코드를 복사할 수 없습니다. 다시 시도해 주세요.';

const codeBlocks = document.querySelectorAll('pre > code');

const copyBlockCode = async (target = null) => {
  if (!target) return;
  try {
    const code = decodeURI(target.dataset.code);

    await navigator.clipboard.writeText(code);
    target.textContent = COPY_BUTTON_TEXT_AFTER;
    setTimeout(() => {
      target.textContent = COPY_BUTTON_TEXT_BEFORE;
    }, COPY_TEXT_CHANGE_OFFSET);
  } catch(error) {
    alert(COPY_ERROR_MESSAGE);
    console.error(error);
  }
}


for (const codeBlock of codeBlocks) {
  const codes = codeBlock.innerHTML.match(/(.*)(\n|.*$)/g);
  
  const processedCodes = codes.reduce((prevCodes, curCode) => prevCodes + 
`<div class="line">${curCode}</div>`, '');
  
  const copyButton = `<button type="button" class="copy-btn" 
data-code="${encodeURI(codeBlock.textContent)}" 
onclick="copyBlockCode(this)">${COPY_BUTTON_TEXT_BEFORE}</button>`;
  
  const codeBody = `<div class="code-body">${processedCodes}</div>`;
  
  const codeHeader = `
  <div class="code-header">
    <span class="red btn"></span>
    <span class="yellow btn"></span>
    <span class="green btn"></span>
    ${copyButton}
  </div>`;
  
  codeBlock.innerHTML = codeHeader + codeBody;
}


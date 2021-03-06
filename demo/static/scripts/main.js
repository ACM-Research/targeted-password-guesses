$("#reset").on("click", e => {
    // By default, resetting would bring back the example values
    // We want to make the fields empty instead
    e.preventDefault();
    $("#name").val("");
    $("#info").val("");
});

$("#guess").on("click", e => {
    e.preventDefault();

    // Get password guesses
    let data = new FormData();
    data.append("realname", $("#realname").val());
    data.append("username", $("#username").val());
    data.append("dob", $("#dob").val());
    data.append("gender", $("#gender").val());
    data.append("country", $("#country").val());
    data.append("twitterid", $("#twitterid").val());
    data.append("about", $("#about").val());
    data.append("status", $("#status").val());

    const $results_ul = $("#results ul").empty();
    for (let i = 0; i < 5; i++) {
        fetch("/guess", {
            method: "POST",
            body: data,
            })
            .then(response => response.json())
            .then(guess => {
                console.log(guess);
                $results_ul.append(`<li>${guess}</li>`);
            })
            .catch(console.error);
    }

    // Run animations if the results element isn't visible yet
    const $results = $("#results");
    if ($results.css("display") === "none") {
        $("form").addClass("slide");
        $results.show();
        setTimeout(function () { return $("form").removeClass("slide"); }, 1000);
    }
    if (window.innerWidth <= 1200)
        document.querySelector("#results").scrollIntoView();
});

// Themes
function reorder_theme_icons() {
    $("header div").append($("#system"))
        .append($("#dark"))
        .append($("#light"))
        .append($("header button.active"));
}

reorder_theme_icons();

$("header div button").on("click", function() {
    if ($(this).parent().hasClass("open")) {
        $("header div button").removeClass("active");
        $(this).addClass("active");
        if (this.id === "system") {
            // Delete the cookie
            document.cookie = "theme=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            $("body").attr("class", "");
        } else {
            document.cookie = "theme=" + this.id + "; SameSite=Lax;";
            $("body").attr("class", this.id);
        }
        $(this).parent().append($(this));
    } else {
        reorder_theme_icons();
    }
    $(this).parent().toggleClass("open");
});


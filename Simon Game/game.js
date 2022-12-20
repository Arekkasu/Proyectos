var wrong_sound = new Audio('sounds/wrong.mp3')

var buttonColours = ['red', 'blue', 'green', 'yellow']
var gamePattern = []

var userClickPattern = []

var start = false

var level = 0

$(document).keypress(function () { 
    if (!start) {

        $("#level-title").text("Level " + level);
        nextSequence();
        start = true;
      }
    
});

function nextSequence() {
    userClickPattern = []

    level++;
    $("#level-title").text("Level " + level);

    let randomNumber = Math.floor(Math.random()*4);
    let randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour)

    console.log()

    $(`#${randomChosenColour}`).fadeOut(100).fadeIn(100);

    playSound(randomChosenColour)
}

$("div [type = 'button']").click(function () {
    let colour = this.id

    $(this).fadeOut(100).fadeIn(100)

    playSound(colour)

    userClickPattern.push(colour)


    animatePress(colour)
    checkAnswer(userClickPattern.length-1)    
})

function playSound(colour) {

    //Funcion que establece el sonido.
    var audio = new Audio("sounds/" + colour + ".mp3");
    audio.play();
  }


function animatePress(currentcolour){

    //Se le agrega el numero debido a que el parametro que recibe es el texto de la ID, mas no la ID como tal
    
    $("#" + currentcolour).addClass("pressed");

    setTimeout(function () {
        $("#" + currentcolour).removeClass("pressed");
      }, 100);

}



function checkAnswer(currentLevel) {

   
    if (gamePattern[currentLevel] === userClickPattern[currentLevel]) {

      console.log("success");

 
      if (userClickPattern.length === gamePattern.length){


        setTimeout(function () {
          nextSequence();
        }, 1000);

      }

    } else {

      wrong_answer()

    }

}

function wrong_answer () {
    $("body").addClass("game-over")
    setTimeout(function () {
        $("body").removeClass("game-over")
      }, 200);
    $("#level-title").text("game-over, press any key to restart game")
    start = false
    level = 0
    gamePattern = []
    wrong_sound.play()
}
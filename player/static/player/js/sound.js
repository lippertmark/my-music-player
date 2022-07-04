function play_sound(slug) {
    const audio_source = document.getElementById('audio_' + slug);
    const play_btn = document.getElementById('play_' + slug);
    const pause_btn = document.getElementById('pause_' + slug);

    play_btn.style.display = 'none';
    pause_btn.style.display = 'block';
    audio_source.play();
}

function pause_sound(slug) {
    const audio_source = document.getElementById('audio_' + slug);
    const play_btn = document.getElementById('play_' + slug);
    const pause_btn = document.getElementById('pause_' + slug);

    play_btn.style.display = 'block';
    pause_btn.style.display = 'none';
    audio_source.pause();

}


function add_to_playlist(slug) {

}
/**
 * Created by TesterCC on 17/8/9.
 */
function refresh_time(){

    var time = new Date();
    document.getElementById('time').textContent = time.toISOString();
}
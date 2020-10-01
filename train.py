#STAMINA STAT THROUGH TRAINING
def train(request, input, id){
    stamina_total = 0;
    
    while (stamina_total < 30 and input = "train"){

        request.session['rations_total'] -= 10
        request.session['stamina_total'] += 1
        
        if (stamina_total == 30) {

            request.session['prompt'] = "Placeholder : Time to go to wor! Type in 'wartime' to go to travel to the battlegraounds."  
        }
        else{
            
            request.session['prompt'] = " Placeholder: Keep training to become a mega superpower! Type 'train' to gain  more stamina."
        }
    }
    return redirect('/game/main')
}

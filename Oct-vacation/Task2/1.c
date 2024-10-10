void InsertSort(int arr[],int len){
    for(int i=1;i<len;i++){
        for(int j=i;j>0;j--){
            if(arr[j]<arr[j-1]){
                int tem=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=tem;
            }else{
                break;
            }
        }
    }
}
void ShellSort(int arr[] ,int len){
    for(int increment=len/2;increment<1;increment/=2){
        for(int i=0;i<increment;i++){
            for(int j=i;j<len-increment;j+=increment){
                if(arr[j]<arr[j+increment]){
                     int tem=arr[j];
                    arr[j]=arr[j+increment];
                    arr[j+increment]=tem;
                }   
            }
        }
    }
}
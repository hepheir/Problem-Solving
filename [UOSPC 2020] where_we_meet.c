#include <stdio.h>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

void main() {
  int N;
  int av_x0, av_y0, av_x1, av_y1; // 친구들이 모두 모일 수 있는 장소 후보
  
  int x, y, w, h;
  int x0, y0, x1, y1;

  int area;

  scanf("%d", &N);

  scanf("%d %d %d %d", &x, &y, &w, &h);
  av_x0 = x - w;
  av_y0 = y - h;
  av_x1 = x + w;
  av_y1 = y + h;

  for (int n=1; n<N; n++) {
    scanf("%d %d %d %d", &x, &y, &w, &h);
    x0 = x - w;
    y0 = y - h;
    x1 = x + w;
    y1 = y + h;

    av_x0 = MAX(av_x0, x0);
    av_y0 = MAX(av_y0, y0);
    av_x1 = MIN(av_x1, x1);
    av_y1 = MIN(av_y1, y1);

    if ((av_x0 > av_x1) && (av_y0 > av_y1)) {
      printf("impossible\n");
      return;
    }
  }

  printf("%d %d\n", av_x0, av_y0);
  return;
}
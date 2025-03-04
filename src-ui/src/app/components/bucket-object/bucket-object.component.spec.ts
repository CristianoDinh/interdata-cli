import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BucketObjectComponent } from './bucket-object.component';

describe('BucketObjectComponent', () => {
  let component: BucketObjectComponent;
  let fixture: ComponentFixture<BucketObjectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BucketObjectComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BucketObjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
